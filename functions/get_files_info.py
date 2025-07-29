import os
def get_files_info(working_directory, directory="."):
        # Create the full path
    full_path = os.path.join(working_directory, directory)

    # Convert both paths to absolute paths
    working_directory_abs = os.path.abspath(working_directory)
    full_path_abs = os.path.abspath(full_path)

    # Validate that the full path is within the working directory
    if not os.path.commonpath([full_path_abs, working_directory_abs]) == working_directory_abs:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if the path is a directory
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    # Initialize a list to hold the directory contents
    contents_info = []

    try:
        # List the contents of the directory
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path) if not is_dir else 0
            contents_info.append(f'{entry}: file_size={file_size} bytes, is_dir={is_dir}')
    except Exception as e:
        return f'Error: {str(e)}'

    # Join the contents info into a single string
    return "\n".join(contents_info)
