import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing from .env file"
    )


# Gemini API Client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# Model
MODEL = "gemini-2.5-flash"


def ask_llm(prompt: str):

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "system_instruction": (
                "You are a helpful College AI Assistant. "
                "Answer students clearly and simply."
            ),
            "max_output_tokens": 500
        }
    )

    return response.text


if __name__ == "__main__":

    question = input("Ask College AI: ")

    try:

        answer = ask_llm(question)

        print("\nAI Response:")
        print(answer)

    except Exception as e:

        print("\nERROR:")
        print(e)