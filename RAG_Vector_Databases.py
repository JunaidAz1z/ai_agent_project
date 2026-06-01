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

import chromadb

client = chromadb.Client()

collection = client.create_collection("pakistan_facts")

# 1. Collection banao "pakistan_facts"
# 2. 5 facts add karo Pakistan ke baare mein
# 3. Query karo: "What is the capital?"
# 4. Top 2 results print karo















