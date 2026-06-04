
                                    #Fixed Size Chunking

# from langchain_text_splitters import CharacterTextSplitter

# text = """
# Pakistan is a country in South Asia.
# It was founded in 1947.
# The capital is Islamabad.
# Lahore is the cultural capital.
# Karachi is the financial hub.
# The population is over 220 million.
# Pakistan has many mountains including K2.
# The national language is Urdu.
# Cricket is the most popular sport.
# Pakistan has a rich cultural heritage.
# """

# splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=100,
#     chunk_overlap=20
# )

# chunks = splitter.split_text(text)

# print(f"Total Chunks: {len(chunks)}")
# print("-" * 40)

# for i, chunk in enumerate(chunks):
#     print(f"Chunk: {i+1} ({len(chunk)}) characters")
#     print(chunk)
#     print("-" * 40)


                                        #Recursive Chunking (Best!)

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text = """
# Pakistan is a country in South Asia.
# It was founded in 1947 by Muhammad Ali Jinnah.
# The capital city is Islamabad.

# Lahore is the cultural capital of Pakistan.
# It is known for its rich history and food.
# The famous Badshahi Mosque is in Lahore.

# Karachi is the largest city and financial hub.
# It is located on the Arabian Sea coast.
# Many businesses are headquartered in Karachi.
# """

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20,
#     separators=["\n\n", "\n", " ", ""]
# )

# chunks = splitter.split_text(text)

# print(f"Total chunks: {len(chunks)}")
# print("-" * 40)
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk}")
#     print("-" * 30)

                                            #Documents Split

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.documents import Document

# docs = [
#     Document(page_content="""Pakistan is a country in South Asia.
# It was founded in 1947 by Muhammad Ali Jinnah.
# The capital is Islamabad. Lahore is cultural capital.
# Karachi is the largest city. Population is 220 million.""",
#         metadata={"source": "pakistan.txt", "page": 1}
#         )
# ]

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20
# )

# chunks = splitter.split_documents(docs)

# print(f"Orignal docs: {len(docs)}")
# print(f"Total Chunks: {len(chunks)}")
# print("-" * 40)

# for i, chunk in enumerate(chunks):
#      print(f"Chunk {i+1}:")
#      print(f"Content: {chunk.page_content}")
#      print(f"Metadata: {chunk.metadata}")  
#      print("-" * 30)


                                         #Chunk Overlap

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=10,
#     chunk_overlap=3
# )

# chunks = splitter.split_text(text)
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk}")


                                        # PDF + Chunking

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("pak.pdf")
# docs = loader.load()

# print(f"Total Pages: {len(docs)}")

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )

# chunks = splitter.split_documents(docs)
# print(f"Total Chunks: {len(chunks)}")
# print(f"Average Chunk size: {sum(len(c.page_content) for c in chunks) // len(chunks)}")

# for i, chunk in enumerate(chunks[:3]):
#     print(f"\nChunk: {i+1}")
#     print(f"Size: {len(chunk.page_content)} chars")
#     print(f"Content: {chunk.page_content}")
#     print(f"Page: {chunk.metadata}")


                                    #Chunking + Vector Store

# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# import shutil, os

# if os.path.exists("./chunks_db"): shutil.rmtree("./chunks_db")

# loader = TextLoader("my_notes.txt")
# docs = loader.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=50,
#     chunk_overlap=20
# )

# chunks = splitter.split_documents(docs)
# print(f"Total Chunks: {len(chunks)}")

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectorscore = Chroma.from_documents(
#     documents=chunks,
#     embedding=embeddings,
#     persist_directory="./chunk_db"
# )

# results = vectorscore.similarity_search(
#     query="What is Ali learning?", k=2
# )

# for doc in results:
#     print(f"{doc.page_content}")


#Ex1

# from langchain_text_splitters import CharacterTextSplitter

# text = """Pakistan, officially known as the Islamic Republic of Pakistan, 
# South Asia ka ek important mulk hai. Yeh 14 August 1947 ko 
# British India se alag hokar azad hua tha. Quaid-e-Azam Muhammad Ali Jinnah 
# is mulk ke founder hain. Aaj Pakistan duniya ke sabse bade population 
# wale mulkon mein shamil hai, jiski abadi 24 crore se zyada hai. 
# Islamabad iski capital hai, jabke Karachi iska sabse bara shehar aur economic hub hai.
# Yeh mulk apni natural beauty ke liye bohot mashhoor hai – zard mountains, 
# khubsurat valleys jaise Hunza, Swat aur Neelum Valley yahan mojood hain. 
# Pakistan ki culture bohot rich hai, jisme Urdu zuban, truck art, 
# Sufi music, aur mehmaan-nawazi shamil hai. Cricket yahan ka sabse 
# popular khel hai. Historical places jaise Mohenjo-Daro, 
# Lahore Fort, Badshahi Mosque aur Taxila is mulk ki purani civilization ko darshate hain.
# Pakistan strategically bohot ahem location par waqia hai, jahan 
# yeh Middle East, Central Asia aur South Asia ko jodta hai. 
# Yeh ek young, energetic aur mehnati qaum ka mulk hai jo 
# apne mustaqbil ko behtar banane ki koshish mein laga hua hai."""

# splitter = CharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=30,
#     separator="\n"
# )

# chunks = splitter.split_text(text)
# print(f"Total Chunks: {len(chunks)}")

# for i, chunk in enumerate(chunks):
#     print(f"Chunk: {i+1}")
#     print(f"{chunk}")
#     print(f"-" * 30)

#Ex2

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text = "Hello how are you bro what are you doing and how is your family"

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=20,
#     chunk_overlap=5
# )
# chunks = splitter.split_text(text)
# for i, chunk in enumerate(chunks):
#     print(f"Chunk: {i+1}: {chunk}")

#Ex3


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
loader = PyPDFLoader("pak.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)
print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"Chunk: {i+1}")
    print(f"Content: {chunk}")
    print(f"-" * 30)

