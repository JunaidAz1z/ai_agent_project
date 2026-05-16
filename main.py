from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Always respond in English"  # ← ye add karo
        },
        {
            "role": "user",
            "content": "Pakistan ke baare mein 3 interesting facts batao"
        }
    ]
)

print(response.choices[0].message.content)