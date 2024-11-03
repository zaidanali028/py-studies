# Activating Virtual Environment
# -------------------------------
# On Windows:
# venv\Scripts\activate

# File Writing Example
# ---------------------
# Using a context manager to write to a file

with open('file_write.txt', 'w') as file:
    # File Modes:
    # 'r' -> Open a file for reading (default mode, file must exist)
    # 'w' -> Open a file for writing (creates a new file or overwrites existing content)
    # 'a' -> Open a file for appending (adds content at the end without overwriting)
    # 'a+' -> Open a file for appending and reading (adds content at the end without overwriting and reading from it)
    # 'x' -> create a file

    # Writing text to the file
    
    file.write('Hola, World')  # Writes "Hola, World" to the file
