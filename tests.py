from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def run_tests():
    # Test 1: Get info for the current directory
    print("Result for main.py: ")
    print(run_python_file("calculator", "main.py"))  # should print the calculator's usage instructions
    print()  # Blank line for separation

    # Test 2: Get info for the 'pkg' directory
    print("Result for 'main.py [3 + 5]':")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))  # should run the calculator... which gives a kinda nasty rendered result
    print()  # Blank line for separation

    # Test 3: Attempt to get info for an outside directory
    print("Result for 'tests.py':")
    print(run_python_file("calculator", "tests.py"))  # Expected error for outside directory
    print()  # Blank line for separation

    print("Result for '../main.py':")
    print(run_python_file("calculator", "../main.py"))  # should return an errot
    print()  # Blank line for separation

    print("Result for 'nonexistant.py':")
    print(run_python_file("calculator", "nonexistent.py"))  # should return an error


if __name__ == "__main__":
    run_tests()