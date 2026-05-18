# Sirf YE LINE change karo — baaki sab same!

# # Groq (LLaMA) — Free 
# from langchain_groq import ChatGroq
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# # OpenAI (GPT-4) 
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4o")

# # Anthropic (Claude)
# from langchain_anthropic import ChatAnthropic
# llm = ChatAnthropic(model="claude-sonnet-4-20250514")

# # Google (Gemini)
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")




#STARTED FROM HERE

# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")

# response = llm.invoke("Tell me about pakistan in one line")

# # print(response.content)
# # print("-" * 30)
# # print(type(response))

# print(response.content)        # actual jawab
# print("---")
# print(response.type)           # "ai"
# print("---")
# print(response.usage_metadata)

#USING MESSAGES
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, SystemMessage
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")

# messages=[
#     SystemMessage("You are a helpful assistant. Always respond in English"),
#     HumanMessage("What is the capital of Pakistan?")
# ]
# response = llm.invoke(messages)

# print(response.content)


#USING PROMPT TEMPLATE

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant. Always respond in English."),
#     ("human", "Tell me a joke about {topic}")
# ])
# prompt = template.invoke({"topic": "Pakistan"})
# print(prompt)
# print("-" * 30)
# response = llm.invoke(prompt)
# print(response.content)


#Ex1

# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, SystemMessage
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# messages= [
#     SystemMessage("You are a python teacher"),
#     HumanMessage("Explain loops in Python in 3 lines")
# ]

# response = llm.invoke(messages)
# print(response.content)
# print("-" * 20)
# print(response.type)
# print("-" * 20)
# print(response.response_metadata)
# print("-" * 20)


#Ex2

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a {role}"),
#     ("human", "Tell me about {topic}")
# ])

# prompt = template.invoke({"role": "Doctor", "topic": "Headache"})
# response = llm.invoke(prompt)
# print(response.content)

# prompt1 = template.invoke({"role": "Chef", "topic": "Biryani"})
# response1 = llm.invoke(prompt1)
# print(response1.content)


#Ex3

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are an expert {subject} teacher"),
#     ("human", "Explain {concept} to a {level} student in {words} words")
# ])

# prompt = template.invoke({"subject":"Python", "concept":"decorators", "level":"beginner", "words":"50"})

# response = llm.invoke(prompt)
# print(response.content)

# Ex4

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a geography expert"),
#     ("human", """Tell me about {country}:
#           - Capital
#           - Population
#           - 2 famous foods
#           - 1 fun fact""")
# ])

# countries = ["Pakistan", "Bangladesh", "Turkey"]
# for country in countries:

#     prompt = template.invoke({"country": country, })

#     response = llm.invoke(prompt)
#     print(response.content)






                                    #Chains PIPE OPERATOR


# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# template = ChatPromptTemplate.from_messages([
#     ("system","You are a senior developer"),
#     ("human", "Tell me one line about {topic}")
# ])

# #without chains
# # prompt = template.invoke({"topic":"python"})
# # response = llm.invoke(prompt)
# # print(response.content)

# #with chains
# chains = template | llm
# response = chains.invoke({"topic":"python"})
# print(response)


#Chain + Output_parser

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system","You are a senior developer"),
#     ("human", "Tell me one line about {topic}")
# ])


# chains = template | llm | parser
# response = chains.invoke({"topic":"python"})
# print(response)


#Chain with loop 

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a geography expert."),
#     ("human", "What is the capital of {country}?")
# ])

# chain = template | llm | parser

# # Multiple countries!
# countries = ["Pakistan", "Turkey", "Japan"]

# for country in countries:
#     response = chain.invoke({"country": country})
#     print(f"{country}: {response}")


#Ex1

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a comedian"),
#     ("human", "Tell me a joke about {topic}")
# ])

# chain = template | llm | parser
# topics = ["cricket", "coding", "karachi"]
# for topic in topics:
#     response = chain.invoke({"topic": topic})
#     print(f"{topic}: {response}")

#Ex2

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a {language} expert"),
#     ("human", "Write a {type} program in {language} that {task}")
# ])

# chain = template | llm | parser
# response = chain.invoke({"language":"Python","type":"simple","task":"prints numbers 1 to 10"})
# print(response)

#Ex3

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a news reporter"),
#     ("human", "Write 3 news headlines about {topic} in {country}")
# ])

# chain1 = template | llm | parser
# response1 = chain1.invoke({"topic":"cricket", "country":"Pakistan"})
# print(response1)

# chain2 = template | llm | parser
# response2 = chain2.invoke({"topic":"technology", "country":"USA"})
# print(response2)


#Ex4

# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are a senior dev"),
#     ("human", "What is {language} best used for? Answer in one line.")
# ])

# chain = template | llm | parser
# languages = ["Python", "JavaScript", "Java", "C++", "Go"]
# for language in languages:

#     response = chain.invoke({"language": language})
#     print(f"{language}:     {response}")














