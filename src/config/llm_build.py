import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("please set the Googgle Api key")


def get_llm():
    return GoogleGenerativeAI(
        model = 'gemini-2.5-flash',
        google_api_key = api_key,
        temperature = 0.3,
        max_output_tokens = 50,
    )
