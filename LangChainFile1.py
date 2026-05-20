
#Prompt Templates

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")  
# parser = StrOutputParser()

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a {role} expert."),
#     ("human", "{question}")
# ])

# partial_template = template.partial(role="Python")

# # Chain banao
# chain = partial_template | llm | parser 

# response1 = chain.invoke({"question": "What is a decorator?"})
# response2 = chain.invoke({"question": "What is async/await?"})

# print(response1)   
# print("-" * 40)
# print(response2)   

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=200)
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     MessagesPlaceholder(variable_name="history"),  # ← history yahan aayegi
#     ("human", "{question}")
# ])

# chain = template | llm | parser
# # History inject karo
# response = chain.invoke({
#     "history": [
#         HumanMessage("Mera naam Ali hai"),
#         AIMessage("Hello Ali!"),
#     ],
#     "question": "Mera naam kya hai?"
# })

# print(response) 


#Models

# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()
# parser = StrOutputParser()

# # Model 1 — Fast
# llm_fast = ChatGroq(model="llama-3.1-8b-instant",
#                     temperature=0.7,
#                     max_tokens=200,)

# # Model 2 — Powerful  
# llm_powerful = ChatGroq(model="llama-3.3-70b-versatile",
#                     temperature=0.7,
#                     max_tokens=200,)

# # Same chain — alag models!
# template = ChatPromptTemplate.from_messages([
# ("system", "you are a helpful assistant."),
# ("human","What is Python in one line?")
# ])
# chain_fast = template | llm_fast |  parser
# chain_powerful = template | llm_powerful  |  parser

# response1 = chain_fast.invoke({})
# response2 = chain_powerful.invoke({})

# print(f"Fast Model:    {response1}")
# print(f"Powerful Model: {response2}")






                                            #MEMORY 



#Manual Memory

# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# history = []

# history.append(HumanMessage("My name is Tom"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

# history.append(HumanMessage("What is my name"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

# history.append(HumanMessage("What i am learning?"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

#Chat Message History

# from langchain_groq import ChatGroq
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# history = InMemoryChatMessageHistory()

# history.add_user_message("My name is kim")
# history.add_ai_message("Hello Kim!")
# history.add_user_message("i am learning PYTHON")
# history.add_ai_message("That's great it is very useful language")

# print(history.messages)

# history.add_user_message("What is my name and what im learning")
# response = llm.invoke(history.messages)
# print(response.content)


# Runnable With Message History (Best Way)

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# template = ChatPromptTemplate.from_messages([
#     ("system", "you are a helpful assistant"),
#     MessagesPlaceholder(variable_name="history"),
#     ("human", "{question}")
# ])

# chain = template | llm | parser

# sessions = {}

# def get_session_history(session_id: str):
#     if session_id not in sessions:
#         sessions[session_id] = InMemoryChatMessageHistory()
#     return sessions[session_id]

# chain_with_memory = RunnableWithMessageHistory(
#     chain,
#     get_session_history,
#     input_messages_key="question",
#     history_messages_key="history"
# )


# r1 = chain_with_memory.invoke({"question": "My name is Ali"}, config=config_ali)
# r12 = chain_with_memory.invoke({"question": "My name is Ahmed"}, config=config_ahmed)
# print(f"AI: {r1}")
# print(f"AI: {r12}")
# r2 = chain_with_memory.invoke({"question": "What is my name?"}, config=config_ali)
# r23 = chain_with_memory.invoke({"question": "What is my name?"}, config=config_ahmed)
# print(f"AI: {r2}")
# print(f"AI: {r23}")
# r3 = chain_with_memory.invoke({"question": "I am learning python"}, config=config_ali)
# r34 = chain_with_memory.invoke({"question": "I am learning java"}, config=config_ahmed)
# print(f"AI: {r3}")
# print(f"AI: {r34}")
# r4 = chain_with_memory.invoke({"question": "What i am learning?"}, config=config_ali)
# r45 = chain_with_memory.invoke({"question": "What i am learning?"}, config=config_ahmed)
# print(f"AI: {r4}")
# print(f"AI: {r45}")



#Ex1

# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# history = []

# history.append(HumanMessage("My name is Tom"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

# history.append(HumanMessage("My city is Chicago"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

# history.append(HumanMessage("My favorite food is Pizza"))
# response = llm.invoke(history)
# history.append(AIMessage(response.content))
# print(f"AI: {response.content}")

# history.append(HumanMessage("what you know about me?"))
# response = llm.invoke(history)
# #history.append([AIMessage(response.content)])
# print(f"AI: {response.content}")



#Ex2

# from langchain_groq import ChatGroq
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# history = InMemoryChatMessageHistory()

# history.add_user_message("My name is Kim")
# history.add_ai_message("Hello Kim")
# history.add_user_message("My age is 25 and i'm ma AI agent maker")
# history.add_ai_message("Good kim this field is filled with too much opportunities")
# history.add_user_message("i lives in washingten")
# history.add_ai_message("This is the awesome city full of techonology")

# print(f"AI: {history.messages}")
# history.add_user_message("Write a summary in 1 to 2 lines about me?")
# response = llm.invoke(history.messages)
# print(response.content)


#Ex3

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant"),
#     MessagesPlaceholder(variable_name="history"),
#     ("human", "{question}")
# ])

# chain = template | llm | parser 
# sessions = {}

# def get_session_id(session_id: str):
#     if session_id not in sessions:
#         sessions[session_id] = InMemoryChatMessageHistory()
#     return sessions[session_id]


# chain_with_memory = RunnableWithMessageHistory(
#     chain,
#     get_session_id,
#     input_messages_key="question",
#     history_messages_key="history"
# )

# config={"configurable": {"session_id": "tom"}}

# r1 = chain_with_memory.invoke({"question": "You have old information"}, config=config)
# print(f"AI: {r1}")

# r2  = chain_with_memory.invoke({"question": "You are a groq llm"}, config=config)
# print(f"AI: {r2}")
# r3  = chain_with_memory.invoke({"question": "You have max tokens 32760"}, config=config)
# print(f"AI: {r3}")
# r4  = chain_with_memory.invoke({"question": "You are a powerful llm for learning"}, config=config)
# print(f"AI: {r4}")
# r5  = chain_with_memory.invoke({"question": "You have 70b information"}, config=config)
# print(f"AI: {r5}")
# r6  = chain_with_memory.invoke({"question": "what i know about you tell me?"}, config=config)
# print(f"AI: {r6}")


#Ex4

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.chat_history import InMemoryChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant"),
#     MessagesPlaceholder(variable_name="history"),
#     ("human", "{question}")
# ])

# chain = template | llm | parser 
# sessions = {}

# def get_session_id(session_id: str):
#     if session_id not in sessions:
#         sessions[session_id] = InMemoryChatMessageHistory()
#     return sessions[session_id]


# chain_with_memory = RunnableWithMessageHistory(
#     chain,
#     get_session_id,
#     input_messages_key="question",
#     history_messages_key="history"
# )

# config_tom={"configurable": {"session_id": "tom"}}
# config_john={"configurable": {"session_id": "John"}}

# r1 = chain_with_memory.invoke({"question": "My name is tom and i'm learning python"}, config=config_tom)
# print(f"AI: {r1}")
# r2  = chain_with_memory.invoke({"question": "YMy name is john and i'm learning web dev"}, config=config_john)
# print(f"AI: {r2}")
# r3  = chain_with_memory.invoke({"question": "what i'm doing"}, config=config_tom)
# print(f"AI: {r3}")
# r4  = chain_with_memory.invoke({"question": "what i'm doing"}, config=config_john)
# print(f"AI: {r4}")




