from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def run_tests():
    # Test 1: Get info for the current directory
    print("Result for lorem.txt: ")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))  # Expected output for current directory
    print()  # Blank line for separation

    # Test 2: Get info for the 'pkg' directory
    print("Result for 'calculator/pkg/morelorem.txt':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))  # Expected output for 'pkg' directory
    print()  # Blank line for separation

    # Test 3: Attempt to get info for an outside directory
    print("Result for 'tmp/temp.txt':")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))  # Expected error for outside directory

if __name__ == "__main__":
    run_tests()