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



# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=10,
#     chunk_overlap=3
# )

# chunks = splitter.split_text(text)
# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i+1}: {chunk}")


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("pak.pdf")
docs = loader.load()

