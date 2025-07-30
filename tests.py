from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def run_tests():
    # Test 1: Get info for the current directory
    print("Result for calculator/main.py: ")
    print(get_file_content("calculator", "main.py"))  # Expected output for current directory
    print()  # Blank line for separation

    # Test 2: Get info for the 'pkg' directory
    print("Result for 'calculator/pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))  # Expected output for 'pkg' directory
    print()  # Blank line for separation

    # Test 3: Attempt to get info for an outside directory
    print("Result for '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))  # Expected error for outside directory
    print()  # Blank line for separation

    # Test 4: Attempt to get info for a parent directory
    print("Result for file not exist:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))  # Expected error for outside directory

if __name__ == "__main__":
    run_tests()