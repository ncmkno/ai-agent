from functions.write_file_content import write_file
from functions.run_python import run_python_file


def test():
    # Test write_file function
    print("Testing write_file function:")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    print("\nTesting run_python_file function:")
    
    # Test valid Python file execution
    result = run_python_file("calculator", "main.py")
    print("Test 1 - calculator/main.py:")
    print(result)
    print()
    
    # Test valid Python file execution (tests.py)
    result = run_python_file("calculator", "tests.py")
    print("Test 2 - calculator/tests.py:")
    print(result)
    print()
    
    # Test file outside working directory (should return error)
    result = run_python_file("calculator", "../main.py")
    print("Test 3 - ../main.py (outside working directory):")
    print(result)
    print()
    
    # Test non-existent file (should return error)
    result = run_python_file("calculator", "nonexistent.py")
    print("Test 4 - nonexistent.py:")
    print(result)
    print()


if __name__ == "__main__":
    test()
