# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("1275655\n")
        file.write("Another line here.")
        print("File 'my_file.txt' created successfully and data written.")
except PermissionError:
    print("Permission denied to create file.")
except Exception as e:
    print("Error:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read file.")
except Exception as e:
    print("Error:", e)
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("\nAppending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.")
        print("Data appended to 'my_file.txt' successfully.")
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to append file.")
except Exception as e:
    print("Error:", e)
finally:
    print("File appending process completed.")
