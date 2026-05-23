
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()
llm = ChatGroq(model="llama-3.3-70b-versatile")

loader = PyPDFLoader("pak.pdf")
docs = loader.load()

print(f"Total Pages: {len(docs)}")
print("-" * 30)

all_content = ""
for doc in docs:
    all_content += doc.page_content

document_content = all_content[:6000]

template = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant. 
                 Answer questions based ONLY on the 
                 provided document."""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Document: {document}\n\nQuestion: {question}")
])

chain = template | llm | parser

sessions = {}

def get_sessions_info(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = InMemoryChatMessageHistory()
    return sessions[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_sessions_info,
    input_messages_key="question",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "tom"}}

print("PDF loaded! Sawaal poochho. 'exit' se band karo.")
print("-" * 30)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = chain_with_memory.invoke(
        {
            "document": document_content, 
            "question": user_input
        },
        config=config
    )
    print(f"AI: {response}")
    print("-" * 30)