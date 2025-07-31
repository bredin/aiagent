import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file
from functions.schema_declarations import *


def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided. Please provide a prompt as a command line argument.")
        sys.exit(1)
    verbose = (len(sys.argv) > 2) and (sys.argv[2] == "--verbose")

    # system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    system_prompt = """
You are a helpful AI coding agent.
When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    prompt = sys.argv[1]

    from functions.schema_declarations import (
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    )
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )


    load_dotenv()  # Load environment variables from .env file
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)

    model = "gemini-2.0-flash-001"

    response = client.models.generate_content(model=model, 
                                              contents=prompt,
                                              config=types.GenerateContentConfig(
                                                  system_instruction=system_prompt,
                                                  tools=[available_functions]
                                                  )
                                              )

    if verbose:
        print(f"User prompt: {prompt}")

    if hasattr(response, 'function_calls') and response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")


        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:   
        print(response.text)


if __name__ == "__main__":
    main()
