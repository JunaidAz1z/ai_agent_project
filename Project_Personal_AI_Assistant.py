                                #PERSONAL AI ASSISTANT

from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.tools import tool
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()

# ─── Tools ───────────────────────────────
@tool
def get_weather(city: str) -> str:
    """Get weather for a Pakistani city."""
    weather = {
        "karachi": "32C Humid",
        "lahore": "35C Sunny",
        "islamabad": "28C Cloudy"
    }
    return weather.get(city.lower(), "City not found")

@tool
def calculator(a: float, b: float, opr: str) -> float:
    """Calculator for math operations: add, subtract, multiply, divide"""
    opr = opr.lower().strip()
    if opr in ["+", "add", "plus"]:
        return a + b
    elif opr in ["-", "subtract", "minus"]:
        return a - b
    elif opr in ["*", "multiply", "times"]:
        return a * b
    elif opr in ["/", "divide", "divided"]:
        return a / b
    else:
        return f"Invalid operator: {opr}"

@tool
def get_info(topic: str) -> str:
    """Get information about Pakistani cities only."""
    info = {
        "lahore": "Lahore is cultural capital of Pakistan",
        "karachi": "Karachi is financial hub of Pakistan",
        "islamabad": "Islamabad is capital of Pakistan"
    }
    return info.get(topic.lower(), "Topic not found")

tools = [get_weather, calculator, get_info]
tools_dict = {t.name: t for t in tools}
llm_with_tools = llm.bind_tools(tools)

# ─── Document Load ────────────────────────
loader = TextLoader("my_notes.txt")
docs = loader.load()
document_content = docs[0].page_content

# ─── Memory Setup ─────────────────────────
sessions = {}

def get_session_history(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = InMemoryChatMessageHistory()
    return sessions[session_id]

# ─── Template ─────────────────────────────
template = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful personal assistant.

Rules:
1. If user tells you their name or info in conversation — remember it!
   Use conversation memory — NOT document for this!
2. For questions about user's background — use the document
3. For weather — use get_weather tool
4. For math — use calculator tool
5. For city info — use get_info tool
6. NEVER say 'topic not found' for personal questions!"""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Document: {document}\n\nQuestion: {question}")
])

chain = template | llm | parser

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "user_session"}}

# ─── Loop ─────────────────────────────────
print("Personal AI Assistant Ready! 'exit' se band karo.")
print("-" * 40)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Tool check
    tool_response = llm_with_tools.invoke(user_input)

    if tool_response.tool_calls:
        for tool_call in tool_response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            result = tools_dict[tool_name].invoke(tool_args)
            print(f"AI: {result}")
    else:
        response = chain_with_memory.invoke(
            {
                "document": document_content,
                "question": user_input
            },
            config=config
        )
        print(f"AI: {response}")

    print("-" * 40)


                                        






