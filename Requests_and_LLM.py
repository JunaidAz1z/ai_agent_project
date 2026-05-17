# import requests

# # Ek user ka data lo
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# # Status code check karo
# print(response.status_code)   # 200 = success

# # Data dekho
# data = response.json()
# # print(data)

# print(f"Naam: {data['name']}")
# print(f"Email: {data['email']}")
# print(f"Phone: {data['phone']}")

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")

# users = response.json()

# print(f"Total users : {len(users)}")

# for user in users:
#     print(f"Id: {user['id']}. {user['name']} - {user['email']}")

# import requests

# new_user = {
#      "name": "Ali Khan",
#     "email": "ali@example.com",
#     "phone": "0300-1234567"
# }

# response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)

# print(response.status_code)
# print(response.json())



# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# # Status code check karo
# if response.status_code == 200:
#     data = response.json()
#     print(f"Success! Name: {data['name']}")

# elif response.status_code == 404:
#     print("User not found!")

# elif response.status_code == 401:
#     print("API key incorrect!")

# else:
#     print(f"Error : {response.status_code}")


#Ex1

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users/5")

# data = response.json()

# print(f"Name: {data['name']} - {data['email']} - {data['phone']}")

#Ex2

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# posts = response.json()

# for post in posts[:5]:
#     print(f"Title: {post['title']}")

#Ex3

#import requests

# new_post = {
#      "title": "Mera Pehla Post",
#      "body": "Ye mera pehla REST API post hai",
#      "userId": 1
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
# print(response.json()['id'])

#Ex4

# import requests

# try:
#    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
#    response.raise_for_status()
#    data = response.json()
#    print(f"{data['name']}")

# except requests.exceptions.HTTPError as e:
#    print(f"User not found : {e}")



# import requests
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# response.raise_for_status()
# user = response.json()

# print(f"User: {user['name']}")
# print("-" * 40)

# groq_res = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a funny comedian. Always respond in English"
#         },
#         {
#             "role": "user",
#             "content": f"Write a funny intro for this person: "
#                        f"Name: {user['name']}, "
#                        f"Email: {user['email']}, "
#                        f"City: {user['address']['city']}, "
#                        f"Company: {user['company']['name']}"
#         }
#     ]
# )

# print(groq_res.choices[0].message.content)



                                            #Temperature / Tokens




# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.1,
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant"
#         },
#         {
#             "role": "user",
#             "content": "Write 2 lines story"
#         }
#     ]
# )
# print("Low Temp: ", response.choices[0].message.content)

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=1.7,
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant"
#         },
#         {
#             "role": "user",
#             "content": "Write 2 lines story"
#         }
#     ]
# )
# print("High Temp: ", response.choices[0].message.content)\


# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# # Chota jawab
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=20,          # ← sirf 20 tokens
#     messages=[
#         {"role": "user", "content": "Tell me about pakistan"}
#     ]
# )
# print("Short:", response.choices[0].message.content)
# print("-" * 40)

# # Lamba jawab
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=500,         # ← 500 tokens
#     messages=[
#         {"role": "user", "content": "Tell me about pakistan"}
#     ]
# )
# print("Long:", response.choices[0].message.content)


                        #Using Tokens and Temperature both

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# # Chota jawab
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.1,
#     # max_tokens=50,          
#     messages=[
#         {"role": "system", "content": "You are a python expert"},
#         {"role": "user", "content": "Write a function to check if a number is prime"}
#     ]
# )
# print("Short:", response.choices[0].message.content)
# print("-" * 40)

# # Lamba jawab
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=1.5,
#     # max_tokens=50,        
#     messages=[
#         {"role": "system", "content": "You are a python expert"},
#         {"role": "user", "content": "Write a function to check if a number is prime"}
#     ]
# )
# print("Long:", response.choices[0].message.content)


                                        #Using Streaming

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# stream = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=1.7,
#     max_tokens=2000,
#     stream=True,
#     messages=[
#         {"role":"system", "content":"You are a helpful assistant. Alwasy respond in English"},
#         {"role":"user", "content":"Tell me about pakistan"}
#     ]
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="", flush=True)
# print()



#Ex1

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# stream = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=2300,
#     stream=True,            
#     messages=[
#         {"role": "user", "content": "Count from 1 to 10 with a fun fact about each number"}
#     ]
# )


# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="", flush=True)

# print() 


#Ex2

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# stream = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=1.5,
#     max_tokens=200,
#     stream=True,
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Always speak english"
#         },
#         {
#             "role": "user",
#             "content": "My name is Tom. Write a short poem about me"
#         },
#     ]
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         text = chunk.choices[0].delta.content
#         print(text, end="", flush=True)
# print()

#Ex3

# import time
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# question = "Tell me a short story about a robot in Pakistan"

# # ================================
# # Test 1 — Without Streaming
# # ================================
# print("Test 1 — Without Streaming")
# print("-" * 40)

# start = time.time()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=200,
#     stream=False,        
#     messages=[
#         {"role": "user", "content": question}
#     ]
# )

# end = time.time()

# print(response.choices[0].message.content)
# print(f"\nBina Streaming Time: {end - start:.2f} seconds")
# print("-" * 40)

# # ================================
# # Test 2 — With Streaming 
# # ================================
# print("\nTest 2 — With Streaming")
# print("-" * 40)

# start = time.time()

# stream = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=200,
#     stream=True,         
#     messages=[
#         {"role": "user", "content": question}
#     ]
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#             print(chunk.choices[0].delta.content, end="", flush=True)

# end = time.time()
# print()
# print(f"Streaming Total Time: {end - start:.2f} seconds")
# print("-" * 40)