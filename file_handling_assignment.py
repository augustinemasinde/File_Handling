

def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is a number: 12345\n")
            file.write("Python file handling example.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line 1.\n")
            file.write("This is an appended line 2.\n")
            file.write("End of file example.\n")
        print("Lines appended successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to write to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
