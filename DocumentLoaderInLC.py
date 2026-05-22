#TEXT FILE LOADER
# from langchain_community.document_loaders import TextLoader

# # File load karo
# loader = TextLoader("my_notes.txt")
# docs = loader.load()

# # Dekho kya aaya
# print(f"Total documents: {len(docs)}")
# print(f"Content: {docs[0].page_content}")
# print(f"Metadata: {docs[0].metadata}")

#PDF LOADER
# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("cv.pdf")
# docs = loader.load()

# print(f"Total Pages: {len(docs)}")

# for i, doc in enumerate(docs):
#     print(f"Page {i+1} {doc.page_content[:1000]}...")
#     print(f"Metadata: {doc.metadata}")
#     print("-" * 30)

#WEB BASE LOADER
# from langchain_community.document_loaders import WebBaseLoader
# from dotenv import load_dotenv
# import os
# import bs4

# load_dotenv()
# os.environ["USER_AGENT"] = "my_app/1.0"

# # Sirf article content lo — baaki ignore karo
# loader = WebBaseLoader(
#     "https://en.wikipedia.org/wiki/Pakistan",
#     bs_kwargs={
#         "parse_only": bs4.SoupStrainer(
#             "div",
#             attrs={"id": "mw-content-text"}  # ← sirf article div lo
#         )
#     }
# )

# docs = loader.load()

# # Clean content
# print(f"Content length: {len(docs[0].page_content)}")
# print(docs[0].page_content[:1000])


#LLM WITH TEXTLOADER
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.document_loaders import TextLoader
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# loader = TextLoader("my_notes.txt")
# docs = loader.load()

# template = ChatPromptTemplate.from_messages([
#     ("system", "Answer questions based on the provided document only."),
#     ("human", "Document:\n{document}\n\nQuestion: {question}")
# ])

# chain = template | llm | parser

# response = chain.invoke({"document":docs, "question": "what i want to become?"})
# print(response)

#TEXTSPLITER

# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = TextLoader("my_notes.txt")
# docs = loader.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20
# )
# chunks = splitter.split_documents(docs)
# print(f"Total chunks: {len(chunks)}")

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk.page_content}")
#     print("-" * 30)


#Ex1

# from langchain_groq import ChatGroq
# from langchain_community.document_loaders import TextLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# loader = TextLoader("my_notes.txt")
# docs = loader.load()
# template = ChatPromptTemplate.from_messages([
#     ("system", "answer the qestions based on the provided document only."),
#     ("human", "document\n{document}\n\nQuestion: {question}")
# ])

# chain = template | llm | parser

# response = chain.invoke({"document": docs, "question": "what are the goals?"})
# print(response)

#Ex2

# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = TextLoader("my_notes.txt")
# docs = loader.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=50,
#     chunk_overlap=10
# )
# chunks = splitter.split_documents(docs)

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk.page_content}")
#     print("-" * 30)

#Ex3

# from langchain_groq import ChatGroq
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# import bs4
# import os
# load_dotenv()
# os.environ["USER_AGENT"] = "my_app/1.0"
# llm = ChatGroq(model="llama-3.3-70b-versatile")

# parser = StrOutputParser()

# loader = WebBaseLoader("https://en.wikipedia.org/wiki/Pakistan",
# bs_kwargs={"parse_only": bs4.SoupStrainer("div", attrs={"id": "mw-content-text"})
#                        })
# docs = loader.load()

# print(f"Content length: {len(docs[0].page_content) }")
# content = docs[0].page_content[:3000]

# template = ChatPromptTemplate.from_messages([
#     ("system", "answer the questions based on provided document"),
#     ("human", "Document: {document} Question:{question}")
# ])

# chain = template | llm | parser
# response = chain.invoke({"document":content, "question": "what is the motto?"})
# print(response)

#Ex4 
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# import os

# load_dotenv()
# os.environ["USER_AGENT"] = "my_app/1.0"

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# parser = StrOutputParser()

# loader = PyPDFLoader("samplepdf.pdf")
# docs = loader.load()

# print(f"Total pages: {len(docs)}")
# print("-" * 30)

# first_page = docs[0].page_content[:2000]

# template = ChatPromptTemplate.from_messages([
#         ("system", "you need to summarize the content that provided you"),
#         ("human", "document: {document} Question: {question}")
# ])

# chain = template | llm | parser

# response = chain.invoke({
#     "document":first_page,
#     "question": "summarize the content of first page"
# })
# print(response)
