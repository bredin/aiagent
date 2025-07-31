import os
from functions.config import CHARACTER_LIMIT

def get_file_content(working_directory, file_path):

    # Convert both paths to absolute paths
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.join(working_directory_abs, file_path)

    print(f"Working Directory: {working_directory_abs}")
    print(f"File Path: {file_path_abs}")

    # Check if the file_path is outside the working_directory
    if not os.path.commonpath([file_path_abs, working_directory_abs]) == working_directory_abs:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Check if the file_path is a regular file
    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        # Read the file
        with open(file_path_abs, 'r') as file:
            content = file.read(CHARACTER_LIMIT)

        # Truncate if necessary
#        if len(content) > CHARACTER_LIMIT:
#            content = content[:CHARACTER_LIMIT] + f' [...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'

        return content

    except Exception as e:
        return f'Error: {str(e)}'
    
