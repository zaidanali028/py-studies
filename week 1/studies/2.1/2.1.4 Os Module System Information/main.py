import os
import signal

# os.abort() immediately terminates the current process and raises the SIGABRT signal.
# In Unix-like systems, SIGABRT indicates that a process has been aborted due to an error.
# It returns an exit code of 3 in Windows.

# Example of raising an exception and aborting the program
# def risky_operation():
#     # Simulate an unrecoverable error
#     raise ValueError("An error occurred!")

# try:
#     risky_operation()
# except ValueError as e:
#     print("Caught an exception:", e)
#     # Abort the program if an exception is caught
#     os.abort()

# This line will not be executed due to os.abort()
# print("This line will not be executed. [Because of the abortion]")

# Display strings used by the os module to refer to directories
print("Current directory symbol:", os.curdir)  # Returns '.' - current directory
print("Parent directory symbol:", os.pardir)   # Returns '..' - parent directory

# Get the pathname separator for the operating system
print("Path separator:", os.sep)                # '/' for Unix and '\\' for Windows
print("Alternative path separator:", os.altsep) # Alternative path separator, if any
print("Extension separator:", os.extsep)        # Typically '.' for file extensions
print("Path separator for lists:", os.pathsep)  # Used to separate multiple paths
print("Default search path for executables:", os.defpath)  # Default paths for executables
print("Null device (used to discard output):", os.devnull)  # Device to which no data is written

# Uncomment to execute a Python script
# os.execl('/usr/bin/python3', 'python', '/home/ali/my-Scripts/2.1/2.1.4 Os Module System Information/execute.py')

# Get the current process ID
process_id = os.getpid()

# Send a SIGINT signal to the current process
# This simulates the effect of pressing Ctrl+C
# os.kill(process_id, signal.SIGINT)
# print("Current process ID:", os.getpid())

# Execute a shell command to print 'hello world'
os.system("echo 'hello world'")

# Get and print process times for the current process
print("Process times:", os.times())

# Wait for a child process to change state (uncomment if you have child processes)
# -1 pid -> waits for any child process
# print("Waiting for child process:", os.waitpid(-1, 0))

# Generate random bytes
print("Random bytes:", os.urandom(45))  # Generate 45 random bytes
