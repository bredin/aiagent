import os
def write_file(working_directory, file_path, content):
    # Convert both paths to absolute paths
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.join(working_directory_abs, file_path)

    # Check if the file_path is outside the working_directory
    if not os.path.commonpath([file_path_abs, working_directory_abs]) == working_directory_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        # Write the content to the file
        with open(file_path_abs, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
    