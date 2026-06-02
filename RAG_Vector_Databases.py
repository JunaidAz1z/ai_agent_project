                                        #Basic ChromaDB

# import chromadb

# # Client banao — local storage
# client = chromadb.Client()

# # Collection banao — jaise SQL mein table!
# collection = client.create_collection("my_first_collection")

# # Documents add karo
# collection.add(
#     documents=[
#         "Ali lives in Lahore Pakistan",
#         "Ali is learning Python and LangChain",
#         "Lahore is the cultural capital of Pakistan",
#         "Ali wants to become an AI Engineer",
#         "Python is used for Machine Learning"
#     ],
#     ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
#     # har document ka unique ID hona chahiye!
# )

# print("Documents added!")
# print(f"Total documents: {collection.count()}")

                                            #With Query

# import chromadb

# client = chromadb.Client()
# collection = client.create_collection("my_collection")

# collection.add(
#     documents=[
#         "Ali lives in Lahore Pakistan",
#         "Ali is learning Python and LangChain",
#         "Lahore is the cultural capital of Pakistan",
#         "Ali wants to become an AI Engineer",
#         "Python is used for Machine Learning"
#     ],
#     ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
# )

# # Query karo!
# results = collection.query(
#     query_texts=["Where does Ali live?"],  # sawaal
#     n_results=2                             # top 2 results
# )

# print("Query: Where does Ali live?")
# print("-" * 40)
# print(f"Results: {results['documents']}")
# print(f"Distances: {results['distances']}")



#Persistent Storage - Disk ma data save rahy

# import chromadb

# client = chromadb.PersistentClient(path="./my_vectordb")

# collection = client.get_or_create_collection("my_docs")

# collection.add(
#     documents=[
#         "Ali lives in Lahore",
#         "Ali is learning AI",
#         "Lahore is in Punjab"
#     ],
#     ids=["1", "2", "3"]
# )

# print(f"Saved! Total: {collection.count()}")


                                    # LangChain + ChromaDB

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_core.documents import Document
# from langchain_chroma import Chroma

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# docs = [
#     Document(page_content="Ali lives in Lahore Pakistan",
#              metadata={"source": "notes.txt", "page": 1}),
#              Document(page_content="Ali is learning Python and LangChain",
#              metadata={"source": "notes.txt", "page": 1}),
#     Document(page_content="Lahore is cultural capital of Pakistan",
#              metadata={"source": "wiki.txt", "page": 2}),
#     Document(page_content="Ali wants to become AI Engineer",
#              metadata={"source": "notes.txt", "page": 1}),
#     Document(page_content="Python is used for Machine Learning",
#              metadata={"source": "wiki.txt", "page": 3}),
# ]

# vector_store = Chroma.from_documents(
#     documents=docs,
#     embedding=embeddings,
#     persist_directory="./chroma_db"
# )

# print("Vector Store Ready!")
# print(f"Total Docs: {vector_store._collection.count()}")

                                        #Similarity Search 

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# embeddings = HuggingFaceEmbeddings(
#     model="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectorstore = Chroma(
#     persist_directory="./chroma_db",
#     embedding_function=embeddings
# )

# query = "Where dose Ali live?"
# results = vectorstore.similarity_search(query, k=2)

# print(f"Query: {query}")
# print("-" * 30)
# for i, doc in enumerate(results):
#     print(f"Result: {i+1} {doc.page_content}")
#     print(f"Source: {doc.metadata}")


                                            #Score Search 

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectors_store = Chroma(
#     persist_directory="./chroma_db",
#     embedding_function=embeddings
# )

# query = "Where does Ali live?"
# results = vectors_store.similarity_search_with_score(query, k=3)

# print(f"Query: {query}")
# print("-" * 30)

# for doc, score in results:
#     print(f"Score: {score:.2f} | {doc.page_content}")

                                        #Retriver

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectors_store = Chroma(
#     persist_directory="./chroma_db",
#     embedding_function=embeddings
# )

# retriver = vectors_store.as_retriever(
#     search_kwargs={"k": 2}
# )

# docs= retriver.invoke("What ali is learning?")
# for doc in docs:
#     print(doc.page_content)






#Ex1

# import chromadb

# client = chromadb.Client()

# collection = client.create_collection("pakistan_facts")

# collection.add(
#     documents=[
#         "Pakistan is home to K2, the world's second-highest mountain",
#         " Over 70 of the world's hand-stitched soccer balls are produced in the city of Sialkot.",
#         "Islamabad is the most beautiful city in the world!",
#         "Islamabad is the capital of Pakistan",
#         "The country contains Mohenjo-Daro, a remarkably planned settlement of the ancient Indus Valley Civilization that dates back to 3300 BCE."
#     ],
#     ids=["1", "2", "3", "4", "5"]
# )

# results = collection.query(
#     query_texts=["What is the capital?"],
#     n_results=2
# )

# print(f"Query: What is the capital?")
# print("-" * 40)
# print(f"Results: {results['documents']}")
# print(f"Distance: {results['distances']}")



#Ex2

# import chromadb

# client = chromadb.PersistentClient(path="./my_db")
# collection = client.get_or_create_collection("my_pookie")

# collection.add(
#     documents=[
#         "My name is Tom",
#         "I am from Chicago",
#         "I'm a AI Agent maker",
#         "my skills are in python, react",
#         "I love programming"
#     ],
#     ids=["1", "2", "3", "4", "5"]
# )

# results = collection.query(query_texts=["What are my skills?"],
#                      n_results=2      
#                            )
# print(f"Query: What is the capital?")
# print("-" * 40)
# print(f"Results: {results['documents']}")
# print(f"Distance: {results['distances']}")



#Ex3

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_core.documents import Document
# from langchain_chroma import Chroma

# embeddigs = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# docs = [
#     Document(page_content="Inheretance",
#              metadata={"source": "text.txt", "page": 1}),
#     Document(page_content="Abstraction",
#              metadata={"source": "tab.txt", "page": 3}),
#     Document(page_content="List in python",
#              metadata={"source": "text.txt", "page": 2}),
#     Document(page_content="Machine learning is used in AI",
#              metadata={"source": "aifile.txt", "page": 1}),
#     Document(page_content="Genrative AI",
#              metadata={"source": "Num.txt", "page": 2}),
#     Document(page_content="LangChain",
#              metadata={"source": "text.txt", "page": 1}),

# ]

# vectorstore= Chroma.from_documents(
#     documents=docs,
#     persist_directory="./my_db",
#     embedding=embeddigs
# )

# results = vectorstore.similarity_search_with_score(query="What is machine learning",k=2)

# print(f"Query: What is machine learning")
# print("-"*30)
# for doc, score in results:
#     print(f"Score: {score:.2f} | {doc.page_content}")



#Ex4

# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# from langchain_core.documents import Document

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# docs = [
#     Document(
#         page_content="Python is an interpreted language",
#         metadata={"source": "py.txt", "page": 39}),
#     Document(
#         page_content="Java is OOP programming",
#         metadata={"source": "java.txt", "page": 12}),
#     Document(
#         page_content="Python is used in AI",
#         metadata={"source": "py.txt", "page": 9}),
#     Document(
#         page_content="AI is model that contains billions of data",
#         metadata={"source": "ai.txt", "page": 21}),
#     Document(
#         page_content="AI means you are doing work automatically",
#         metadata={"source": "ai.txt", "page": 1}),
#     Document(
#         page_content="For learning programming you need to learn basic programming concents of that language",
#         metadata={"source": "py.txt", "page": 39}),
#     Document(
#         page_content="Learning python is very easy",
#         metadata={"source": "py.txt", "page": 39}),
#     Document(
#         page_content="I am a python developer",
#         metadata={"source": "py.txt", "page": 39}),
# ]

# vector_store= Chroma.from_documents(
#     documents=docs,
#     persist_directory="./my_db",
#     embedding=embeddings
# )

# retriver = vector_store.as_retriever(
#     search_kwargs={"k": 3}
# )

# result = retriver.invoke("Hpw to learn programming")

# for doc in result:
#     print(doc.page_content)















