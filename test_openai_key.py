import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
print("🔑 OpenAI API Key:", api_key[:10] + "..." if api_key else "None")

# Create OpenAI client
client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello, who are you?"}],
    )
    print("✅ API Key is working.")
    print("🤖 Response:", response.choices[0].message.content)
except Exception as e:
    print("❌ API Key is NOT working.")
    print("🚫 Error:", e)
