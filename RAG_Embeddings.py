                                        #Basic Embedding
# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # Text ko numbers mein badlo
# text = "Ali lives in Lahore Pakistan"
# vector = embeddings.embed_query(text)

# print(f"Text: {text}")
# print(f"Vector length: {len(vector)}")
# print(f"First 5 numbers: {vector[:5]}")

                                    #Multiple Text Embeddings

# from langchain_huggingface import HuggingFaceEmbeddings

# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# texts = [
#     "Tom lives in Washington",
#     "Python is a programming language",
#     "Washington is capital of USA",
#     "Machine learning is part of AI"
# ]

# vectors = embeddings.embed_documents(texts)

# print(f"Total vectors: {len(vectors)}")
# print(f"Each vector length: {len(vectors[0])}")

# for i, text in enumerate(texts):
#     print(f"\nText {i+1}: {text}")
#     print(f"First 3 numbers: {vectors[i][:3]}")


#                                             Similarity Check

# from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# q1 = "Tom lives in washington."
# q2 = "Tom is from washington city."
# q3 = "python is a programming language."

# v1 = embeddings.embed_query(q1)
# v2 = embeddings.embed_query(q2)
# v3 = embeddings.embed_query(q3)

# def similarity(a, b):
#     a = np.array(a)
#     b = np.array(b)

#     np.dot(a, b)

#     np.linalg.norm(a)
#     np.linalg.norm(b)

#     return np.dot(a, b)/ (np.linalg.norm(a) * np.linalg.norm(b))

# # Part 1: np.dot(a, b)
# # ────────────────────
# # Dono vectors multiply karo — dot product

# # a = [1, 2, 3]
# # b = [4, 5, 6]
# # dot = (1*4) + (2*5) + (3*6)
# #     = 4 + 10 + 18
# #     = 32

# # Part 2: np.linalg.norm(a) * np.linalg.norm(b)
# # ──────────────────────────────────────────────
# # Dono vectors ki sizes multiply karo

# # norm(a) = 3.74
# # norm(b) = 8.77
# # product = 3.74 * 8.77 = 32.8


# # Part 3: Part1 / Part2
# # ─────────────────────
# # 32 / 32.8 = 0.97   similarity

# print(f"S1 vs S2 (similar): {similarity(v1, v2):.4f}")
# print(f"S1 vs S3 (different): {similarity(v1, v3):.4f}")



#Ex1

# from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# texts = [
#      "I love cricket",
#      "Cricket is my favorite sport",
#      "Python is a programming language",
#      "I enjoy playing cricket",
#      "Machine learning is amazing"
# ]
# vectors = embeddings.embed_documents(texts)
# print(f"Total Vectors: {len(vectors)}")
# for i, text in enumerate(texts):
#     print(f"\nText{i+1}: {text}")
#     print(f"First 3 numbers: {vectors[i][:3]}")


#Ex2

# from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# q1 = "Karachi is a big city"
# q2 = "Karachi is the largest city of Pakistan"
# q3 = "Python is used for AI"
# q4 = "Artificial intelligence uses Python"

# v1 = embeddings.embed_query(q1)
# v2 = embeddings.embed_query(q2)
# v3 = embeddings.embed_query(q3)
# v4 = embeddings.embed_query(q4)

# def similarity(a, b):
#     a = np.array(a)
#     b = np.array(b)

#     np.dot(a, b)

#     np.linalg.norm(a)
#     np.linalg.norm(b)

#     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# print(f"S1 vs S2 (similar): {similarity(v1, v2):.4f}")
# print(f"S3 vs S4 (similar): {similarity(v3, v4):.4f}")
# print(f"S1 vs S3 (different): {similarity(v1, v3):.4f}")


#Ex3

# from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# def similarity(a, b):
#     a = np.array(a)
#     b = np.array(b)

#     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# def find_most_similar(query, sentences):
#     query_vector = embeddings.embed_query(query)
#     sentence_vector = embeddings.embed_documents(sentences)

#     best_score = -1
#     best_sentence = ""

#     for i, sent_vector in enumerate(sentence_vector):
#         score = similarity(sent_vector, query_vector)
#         print(f"{sentences[i]} {score:.4f}")

#         if score > best_score:
#             best_score = score
#             best_sentence = sentences[i]
#     return best_sentence, best_score

# query = "Where does Ali live?"
# sentences = [
#     "Ali lives in Lahore",
#     "Ali is learning Python",
#     "Lahore is in Pakistan",
#     "Ali wants to be AI Engineer"
# ]

# print(f"Query : {query}")
# print("-" * 30)
# result, score = find_most_similar(query, sentences)

# print("-" * 30)
# print(f"Most similar: {score:.4f}")



