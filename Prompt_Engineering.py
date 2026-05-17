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

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": """Classify sentiment as POSITIVE or NEGATIVE:

Example 1:
Text: "I love this product!"
Sentiment: POSITIVE

Example 2:
Text: "This is terrible"
Sentiment: NEGATIVE

Now classify:
Text: "Pakistan won the match!"
Sentiment:"""
        }
    ]
)

print(response.choices[0].message.content)