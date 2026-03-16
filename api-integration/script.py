import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY", ""),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

resp = client.chat.completions.create(
    model="gemini-3-flash-preview",
    n=1,
    messages=[
        {"role": "user", "content": "Hey There! Who are you ??"}
    ]
)

print(resp.choices[0].message)
