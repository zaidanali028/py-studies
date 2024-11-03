# Activating a Virtual Environment
# -------------------------------
# On Windows:
# venv\Scripts\activate

# On Linux/macOS:
# source venv/bin/activate

# Opening Files and Using Context Managers
# ----------------------------------------

# Using a context manager to open and close a file automatically
with open('file_read.txt', 'r') as file:
    # file.read(1) - Reads a specific chunk from the file; takes a number as an argument.
    # file.readlines() - Reads every line of the file into a list.
    # file.readline() - Reads a single line from the file.
    
    # Example: Reading line-by-line in a loop
    # for line in file:
    #     print(f"** {line}")

    # Reading a specified chunk size
    size_to_read = 10
    file_contents = file.read(size_to_read)
    print(file_contents)

    # Moving the file pointer with seek()
    # file.seek(0) - Moves the pointer to the beginning of the file
    file.seek(1)
    file_contents = file.read(size_to_read)
    print(file_contents)

    # Reading chunks of a file in a loop
    # while len(file_contents) > 0:
    #     print(file_contents, end="*")
    #     file_contents = file.read(size_to_read)  # Ensure reading new chunk each time

    # Getting the current file pointer position
    print(file.tell())

    # Reading from a file and copying contents to a new file
    # with open('file_read_copy.txt', 'w') as file_copy:
    #     for line in file:
    #         file_copy.write(line)

# Working with Binary Files
# -------------------------

# Copying a binary file (e.g., an image)
# with open('man.jpg', 'rb') as main_image_file:
#     with open('man_copy.jpg', 'wb') as copied_image_file:
#         for b in main_image_file:
#             copied_image_file.write(b)

# Reading and writing a specific chunk size in binary mode
with open('man.jpg', 'rb') as main_image_file:
    with open('man_chunk_copy.jpg', 'wb') as copied_image_file:
        chunk_size = 4096
        chunk_to_write = main_image_file.read(chunk_size)
        while len(chunk_to_write) > 0:
            copied_image_file.write(chunk_to_write)
            chunk_to_write = main_image_file.read(chunk_size)
