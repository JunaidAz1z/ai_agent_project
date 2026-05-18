import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()
#1 Clear & Specific Instructions
#2 Role Playing 

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "system",
#             "content": """You are a senior Python developer 
#                          with 10 years of experience.
#                          Always give practical advice.
#                          Point out bugs clearly."""
#         },
#         {
#             "role": "user",
#             "content": "Review this code: def add(a,b): return a-b"
#         }
#     ]
# )

#Give Examples

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": """Classify sentiment as POSITIVE or NEGATIVE:

# Example 1:
# Text: "I love this product!"
# Sentiment: POSITIVE

# Example 2:
# Text: "This is terrible"
# Sentiment: NEGATIVE

# Now classify:
# Text: "Pakistan won the match!"
# Sentiment:"""
#         }
#     ]
# )

#THINK STEP BY STEP

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
            
#     "role": "user",
#     "content": """A store has 500 items.
#                  30% are electronics.
#                  Of electronics, 40% are phones.
#                  How many phones are there?
                 
#                  Think step by step."""
#         }
#     ]
# )

#OUTPUT FORMAT SPECIFY 

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
            
#     "role": "user",
#     "content": """Give me 5 Python tips.
#    Format:
#    - Tip number
#    - Title (bold)
#    - One line explanation
#    - Code example
   
#    Keep each tip under 3 lines."""
#         }
#     ]
# )

#GIVE CONSTRAINTS

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
            
#     "role": "user",
#     "content": """Explain Machine Learning to a 10 year old.
#    Rules:
#    - No technical jargon
#    - Use simple words only
#    - Maximum 3 sentences
#    - Use a fun analogy"""
#         }
#     ]
# )


#PROMPT USING ALL TECHNIQUES 

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=1000,
#     messages=[
#         {
#             "role": "system",
#             "content": """You are an expert Python teacher 
#                          with 10 years of experience.
#                          Always explain with examples.
#                          Use simple English.
#                          Format responses with clear sections."""
#         },
#         {
#             "role": "user",
#             "content": """Explain Python decorators.
                         
#                          Requirements:
#                          - Start with a real life analogy
#                          - Show simple code example
#                          - Show real world use case
#                          - Maximum 200 words
#                          - Use bullet points
                         
#                          Think step by step."""
#         }
#     ]
# )

# print(response.choices[0].message.content)

# Agent ka system prompt — bohot important!
# system_prompt = """You are an AI agent that helps users.

# Your capabilities:
# - Search the web
# - Write code
# - Analyze data

# Rules:
# - Always think step by step
# - If unsure, ask for clarification
# - Return results in JSON format
# - Never make up information

# Response format:
# {
#     "thought": "what you're thinking",
#     "action": "what you'll do",
#     "result": "final answer"
# }"""

#Ex1

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=1000,
#     messages=[
#         {
#             "role":"system",
#             "content": """You are a senior doctor, you have 15 years of experience in this field. 
#             The patient will tell you the disease. 
#             You have to diagnose the disease 
#             and give 3 suggestions. 
            
#             The answer has to be given in English.
#             Use simple English.
# #           Format responses with clear sections
#             """
#         },
#         {
#             "role":"user",
#             "content":"""Headache, fever and cough.
#                 requriments:
#                     - use bullet points
#             think step by step

#             """
#         }
#     ]
# )
# print(response.choices[0].message.content)


#Ex2

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=1000,
#     messages=[
#         {
#             "role":"user",
#             "content":"""Classify sentiments as poitive or negative.
# Example 1: "happy" - "Positive emotion"
# Example 2: "angry" - "Negative emotion"
# Example 3: "scared" - "Negative emotion"

# Now classify
# - "excited"
# - "sad"
# - "grateful"
#             """
#         }
#     ]
# )
# print(response.choices[0].message.content)

#Ex3

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=1000,
#     messages=[
#         {
#             "role":"user",
#             "content":"""A shop buys items for Rs. 500 each.
#  They sell at 30% profit.
#  They sold 150 items this month.
#  But 10 items were returned.
#  What is total profit?

#  Think step by step
#             """
#         }
#     ]
# )
# print(response.choices[0].message.content)

#Ex4

# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     max_tokens=1000,
#       response_format={"type": "json_object"},
#     messages=[

#         {
#             "role":"system",
#             "content": """You are a 'Career Counselor'
#             with experience of 5 years.
#             user provides you skills, interest, budget.
#             format:
#                 Skills {...}
#                 interest {...}
#                 budget
#             """
#         },
#         {
#             "role":"user",
#             "content":""" skills are Python, react, javascript
#             interest is ai agent ai engineer
#             budget 10000$

# max words 200
# response in json format:
# career_options - {...}
# salry_range - {...}
# required_skills - {...}
# use bullet points
# Think step by step
#             """
#         }
#     ]
# )
# print(response.choices[0].message.content)