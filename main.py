import os
from dotenv import load_dotenv
from google import genai


def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
    load_dotenv()  # Load environment variables from .env file
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)

    model = "gemini-2.0-flash-001"
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(model=model, contents=prompt)

    print("Response from Gemini API:") 
    print(response.text)
    print("Done!")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
