from functions.get_files_info import get_files_info

def run_tests():
    # Test 1: Get info for the current directory
    print("Result for current directory:")
    print(get_files_info("calculator", "."))  # Expected output for current directory
    print()  # Blank line for separation

    # Test 2: Get info for the 'pkg' directory
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))  # Expected output for 'pkg' directory
    print()  # Blank line for separation

    # Test 3: Attempt to get info for an outside directory
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))  # Expected error for outside directory
    print()  # Blank line for separation

    # Test 4: Attempt to get info for a parent directory
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))  # Expected error for outside directory

if __name__ == "__main__":
    run_tests()