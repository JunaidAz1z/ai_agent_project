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

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Alaway respond in english"
    }
]

print("Chatbot is ready to respond...")
print("Write the 'exit' to stop chating.")
print("-"* 40)

while True:
    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break
    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=messages
    )
    ai_reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    print(f"AI: {ai_reply}")
    print("-" * 40)