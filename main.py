import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided. Please provide a prompt as a command line argument.")
        sys.exit(1)

    prompt = sys.argv[1]

    print("Hello from aiagent!")

    load_dotenv()  # Load environment variables from .env file
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)

    model = "gemini-2.0-flash-001"

    response = client.models.generate_content(model=model, contents=prompt)

    print("Response from Gemini API:") 
    print(response.text)
    print("Done!")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()
