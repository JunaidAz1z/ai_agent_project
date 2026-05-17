# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq()

# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role": "system",
#             "content": "Always respond in English"  # ← ye add karo
#         },
#         {
#             "role": "user",
#             "content": "What is the price of gold in pakistan?"
#         },
#         # {
#         #     "role": "assistant",
#         #     "content": "As of my knowledge cutoff, the price of gold in Pakistan was around PKR 130,000 to PKR 140,000 per tola (11.66 grams). However, please note that this information may not be current, and I recommend checking the sources mentioned above for the latest prices."
#         # },
#         # {
#         #     "role": "user",
#         #     "content": "What is the answer of previous question?"
#         # }
#     ]
# )

# print(response.choices[0].message.content)




                                            #ChatBot


# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()
# client = Groq()

# messages = [
#     {
#         "role": "system",
#         "content": "You are a helpful assistant. Alaway respond in english"
#     }
# ]

# print("Chatbot is ready to respond...")
# print("Write the 'exit' to stop chating.")
# print("-"* 40)

# while True:
#     user_input = input("YOU: ")
#     if user_input.lower() == "exit":
#         print("AI: Goodbye!")
#         break
#     messages.append({
#         "role": "user",
#         "content": user_input
#     })

#     response = client.chat.completions.create(
#         model = "llama-3.3-70b-versatile",
#         messages=messages
#     )
#     ai_reply = response.choices[0].message.content

#     messages.append({
#         "role": "assistant",
#         "content": ai_reply
#     })

#     print(f"AI: {ai_reply}")
#     print("-" * 40)


                            #ChatBot Using Streaming

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

messages = [
    {"role":"system", "content":"You are my smart assistant. Always respond in English."}
]

print(f"Chatbot is ready to chat")
print("If you want to stop chating write 'exit' ")
print(f"-" * 40)

while True:

    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    messages.append({
        "role":"user",
        "content":user_input
    })
    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=200,
        stream=True,
        messages=messages
    )

    print("AI: ", end="", flush=True)

    full_reply = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)
            full_reply = full_reply + text

    print()
    print("-" * 40)

    messages.append({
        "role":"assistant",
        "content":full_reply
    })



