import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",             
        contents="Say hello in one sentence."
    )
    print("Response text:", response.text, flush=True)
except Exception as e:
    print("ERROR occurred:", e, flush=True)