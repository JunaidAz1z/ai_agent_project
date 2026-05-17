# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     stream=False,
#     response_format={"type":"json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": "Give me info about Pakistan. Include name, capital, population, and languages."
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)

# print(data)
# print(type(data))


#Same above code USING STREAMING

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# stream = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     stream=True,
#     response_format={"type":"json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": "Give me info about Pakistan. Include name, capital, population, and languages."
#         }
#     ]
# )

# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         text = chunk.choices[0].delta.content

# data = json.loads(text)

# print(f"Name: {data['name']}")
# print(f"Capital: {data['capital']}")
# print(f"Population: {data['population']}")
# print(f"Languages: {data['languages']}")


# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     stream=False,
#     response_format={"type":"json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": "Give me info about Pakistan. Include name, capital, population, and languages."
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)

# print(f"Name: {data['name']}")
# print(f"Capital: {data['capital']}")
# print(f"Population: {data['population']}")
# print(f"Languages: {data['languages']}")
# print(f"Languages: {', '.join(data['languages'])}")

                                #USING LIST OF ITEMS

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     stream=False,
#     response_format={"type":"json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant. Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": """Give me 3 Python topics to learn.
#             Format:{
#             "topics":[
#             {"name": "...", "difficulty": "...", "time": "..."},
#             ]
#             }
#             """
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)

# for topic in data["topics"]:
#     print(f"Topic: {topic['name']}")
#     print(f"Difficulty: {topic['difficulty']}")
#     print(f"Time: {topic['time']}")


#USING ERROR HANDLING

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# try:
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         temperature=0.7,
#         max_tokens=500,
#         response_format={"type": "json_object"},
#         messages=[
#             {
#                 "role": "system",
#                 "content": "Always respond in json format."
#             },
#             {
#                 "role": "user",
#                 "content": "Give me info about Lahore city."
#             }
#         ]
#     )

#     # JSON parse karo
#     data = json.loads(response.choices[0].message.content)
#     print(data)

# except json.JSONDecodeError:
#     print("JSON parse nahi hua!")

# except Exception as e:
#     print(f"Kuch masla hua: {e}")


#Ex1

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": "Give me info about usa. Include name, capital, population and 3 foods"
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)
# print(f"Name: {data['name']}")
# print(f"Capital: {data['capital']}")
# print(f"Population: {data['population']}")
# print(f"Foods: {data['foods']}")


#Ex2

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": """Give me 5 ai agent tools
#             format: {
#             tools:[{"tool_name": "...", "purpose":"...", "difficulty": "..."}]
#             }
# """
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)

# for tool in data['tools']:
#     if tool is not None:
#         print(f"Tool_Name: {tool['tool_name']}")
#         print(f"Purpose: {tool['purpose']}")
#         print(f"Difficulty: {tool['difficulty']}")


#Ex3

# import json
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# name = input("Enter your name: ")
# skills = input("Enter your skills: ")
# experience = input("Enter your experience: ")

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     temperature=0.7,
#     max_tokens=500,
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "Always respond in JSON format."
#         },
#         {
#             "role": "user",
#             "content": """Analyze the resume of this person and return exectly json:
#             {{
#             "name": "person name",
#             "strength": ["strenght1","strength2"],
#             "weakness": ["weakness1", "weakness2"],
#             "job_suggestions": ["job1", "job2", "job3"]
#             }}
#             person details:
#             Name: {name}
#             Skills: {skills}
#             Experience: {experience} years
# """
#         }
#     ]
# )

# raw = response.choices[0].message.content
# data = json.loads(raw)

# print(f"Name: {data['name']}")
# print("-" * 60)
# for s in data['strength']:
#     print(f"Skills: {s}")
# print("-" * 60)
# for w in data['weakness']:
#     print(f"Weakness: {w}")
# print("-" * 60)
# for job in data['job_suggestions']:
#     print(f"Suggested Jobs: {job}")

#Ex4

import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

# goal = input("Enter your goal")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "Always respond in JSON format."
        },
        {
            "role": "user",
            "content": """I want to learn python:
            goals:[{
            "goal":"...",
            "steps":["step1", "step2", "step3"],
            "total_days":"...",
            "difficulty":"..."
        }]
           
"""
        }
    ]
)

raw = response.choices[0].message.content
data = json.loads(raw)

for goal in data['goals']:
    print(f"Goal: {goal['goal']}")
    
    print("Steps:")
    for step in goal['steps']:        
        print(f"  - {step}")
    
    print(f"Total Days: {goal['total_days']}")
    print(f"Difficulty: {goal['difficulty']}")
    print("-" * 40)



















