import os
import platform

# Define the parent directory for file and directory operations
parent_dir = "/home/ali/my-Scripts/2.1/Os Module in Python with Examples"

# Function to print the current working directory
def current_path(): 
    print(os.getcwd()) 
    print() 

# Demonstrating getting and changing the current working directory
print("Current working directory before:")
current_path() 

os.chdir('../')  # Change to the parent directory
print("Current working directory after:")
current_path() 

# --------------------------------------------
# Creating Directories
# --------------------------------------------

# Create a directory named "GeeksforGeeks" within the parent directory
directory = "GeeksforGeeks"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print(f"Directory '{directory}' created.")

# Create another directory named "Geeks" with specific permissions
directory = "Geeks"
mode = 0o666  # Permission mode
path = os.path.join(parent_dir, directory)

os.mkdir(path, mode)
print(f"Directory '{directory}' created with mode {oct(mode)}.")

# --------------------------------------------
# Listing Files and Directories
# --------------------------------------------

# List all files and directories in a specific path
path = "/tmp"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :")
print(dir_list)

# --------------------------------------------
# Removing a File
# --------------------------------------------

# Specify the file to delete
file = 'file1.txt'
location = parent_dir
path_to_delete = os.path.join(location, file)

# Check if the path exists before attempting to remove it
if os.path.exists(path_to_delete):
    os.remove(path_to_delete)
    print(f"'{path_to_delete}' has been removed.")
else:
    print("Path does not exist for the removal operation.")

# --------------------------------------------
# Removing a Directory
# --------------------------------------------

# Remove an empty directory
directory = "Geeks"
path = os.path.join(parent_dir, directory)

if os.path.exists(path):
    os.rmdir(path) 
    print(f"'{path}' has been removed.")
else:
    print("Path does not exist for the removal operation.")

# --------------------------------------------
# Detecting the Operating System
# --------------------------------------------

# Using os.name to detect the OS type
if os.name == 'posix':
    os_type = "Unix-like (Linux, macOS, etc.)"
elif os.name == 'nt':
    os_type = "Windows"
elif os.name == 'java':
    os_type = "Java Virtual Machine"
else:
    os_type = "Unknown OS type"

print(f"os.name: '{os.name}' -> Detected as: {os_type}")

# Using platform.system() for more specific OS identification
exact_os = platform.system()
print(f"platform.system(): '{exact_os}' -> Detected OS name: {exact_os}")

# --------------------------------------------
# File Operations: Reading and Writing
# --------------------------------------------

# Attempt to open and read a file, handling potential IO errors
try:
    filename = 'GFG.txt'
    with open(filename, 'r') as f:  # Use context manager for automatic closing
        text = f.read()
        print("File contents:", text)
except IOError:
    print('Problem reading: ' + filename)

# Create a new file and write to it
fd = "GFG.txt"
with open(fd, 'w') as file:
    file.write("Hello")

# Read from the file to verify the content
with open(fd, 'r') as file:
    text = file.read()
    print("File contents after writing:", text)

# --------------------------------------------
# Renaming a File
# --------------------------------------------

# Rename the file from 'GFG.txt' to 'New.txt'
os.rename(fd, 'New.txt')

# --------------------------------------------
# Getting the Size of a File
# --------------------------------------------

# Get the size of a specific file in bytes
size = os.path.getsize("main.py")
print("Size of 'main.py' is", size, "bytes.")
