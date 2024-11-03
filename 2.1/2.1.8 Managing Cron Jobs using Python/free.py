# running the free command using subprocess
import subprocess
# subprocess allows running shell commands like os.system and os.popen()
import os

# Command to be executed by the job
command = 'free'

# Get the current working directory
current_directory = os.getcwd()

# Path for the output file
output_file_path = os.path.join(current_directory, 'memoryInfo.txt')

# Store the output of the command to a file
with open(output_file_path, 'a') as outputFile:
    outputFile.write('\n' + str(subprocess.check_output(command, shell=True).decode('utf-8')))


