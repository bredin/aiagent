import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # Convert both paths to absolute paths
    working_directory_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory_abs, file_path))

    # Check if the file_path is outside the working_directory
    if not file_path_abs.startswith(working_directory_abs + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Check if the file_path is a regular file
    if not os.path.isfile(file_path_abs):
        return f'Error: File "{file_path}" not found.'

    # Check if the file has a .py extension
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # Run the Python file with the provided arguments
        command = [sys.executable, file_path_abs] + args
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_directory_abs)
        
        # Format the output
        output = []
        if result.stdout:
            output.append(f'STDOUT: {result.stdout.strip()}')
        else:
            output.append('No output produced.')
        if result.stderr:
            output.append(f'STDERR: {result.stderr.strip()}')
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        return "\n".join(output)
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.strip()}'
    except subprocess.TimeoutExpired:
        return 'Error: Execution timed out after 30 seconds.'
    except Exception as e:
        return f'Error: executing Python file: {e}'