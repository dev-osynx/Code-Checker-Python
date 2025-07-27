import os 
import py_compile

def check_python_files(folder="."):
    print(f"Scanning {folder} for Python files with errors...")
    errors = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    py_compile.compile(file_path, doraise=True)
                except py_compile.PyCompileError as e:
                    print(f"Errors in {file_path}: {e}")
                    errors.append(file_path)

    if errors: 
        print(f"Found {len(errors)} Python files with errors.")
        print("Please fix these errors and try again.")

    else:
        print("No Python files with errors found.")

if __name__ == "__main__":
    check_python_files()
                     