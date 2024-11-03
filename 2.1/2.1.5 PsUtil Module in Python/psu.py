from datetime import timedelta  # Import the timedelta class to work with time durations
from sys import argv  # Import argv to access command-line arguments
from time import time  # Import time to work with time-related functions
import psutil as psu  # Import the psutil library as psu for system and process information

# psutil package is a cross-platform library that provides an interface for retrieving information 
# on system utilization (CPU, memory, disks, network, sensors) and managing running processes.
NAME = argv[0]  # Store the name of the script being executed (first command-line argument)

# Define a function to gather system information
def system_info():
    # Calculate the CPU usage over a specified interval (0.1 seconds)
    cpu_in_use = psu.cpu_percent(interval=.1)
    
    # Calculate the system uptime by subtracting the boot time from the current time
    up_time = timedelta(seconds=time() - psu.boot_time())
    
    # Create a dictionary to store system information
    info = {
        "Uptime": up_time,  # Store the uptime in the dictionary
        "CPU in use:": f"{cpu_in_use}%",  # Store the CPU usage percentage
        # Calculate total CPU time by summing the user and system CPU times
        "Time on CPU": timedelta(seconds=psu.cpu_times().system + psu.cpu_times().user),
        # Calculate available memory and convert it to GB
        "Memory in use": f"{psu.virtual_memory().available / (1024**3):,.3f} GB",
        # Calculate free disk space for the root directory and convert it to GB
        "Disk in use": f"{psu.disk_usage('/').free / (1024**3):,.3f} GB",
    }
    
    # Return a formatted string of the system information
    return "\n\n SYSTEM INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()])

# Define a function to gather information about running processes
def process_info():
    # Iterate over all running processes and retrieve specified attributes
    for proc in psu.process_iter(attrs=("name", "cmdline", "pid", "create_time", "cpu_percent", "num_threads", "memory_percent", "cpu_times")):
        # Check if the process name contains "python" and if it matches the script name
        if "python" in proc.info["name"] and (cl := proc.info["cmdline"]) is not None and len(cl) > 0 and NAME in cl[-1]:
            # Calculate the process uptime by subtracting the creation time from the current time
            uptime = timedelta(seconds=time() - proc.info['create_time'])
            
            # Access CPU times safely; if not available, default to 0
            cpu_times = proc.info['cpu_times']
            cpu_time_total = (cpu_times.system if cpu_times.system is not None else 0) + (cpu_times.user if cpu_times.user is not None else 0)

            # Create a dictionary to store process information
            info = {
                "PID": proc.info["pid"],  # Store the process ID
                "Uptime": uptime,  # Store the process uptime
                "CPU in use": f"{proc.info['cpu_percent']}%",  # Store the CPU usage percentage for the process
                # Store the total CPU time used by the process
                "Time on CPU": timedelta(seconds=cpu_time_total),
                "No of threads": proc.info['num_threads'],  # Store the number of threads used by the process
                # Store the memory usage percentage and format it to three decimal places
                "Memory in use": f"{(mem := proc.info['memory_percent']):.3f}%",
                # Calculate the actual memory usage in GB based on the total virtual memory
                "Memory usage": f"{psu.virtual_memory().total * (mem / 100) / (1024**3):,.3f} GB"
            }

            # Return a formatted string of the process information
            return "\n\n PROCESS INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()])

# Example usage: Call the functions to print system and process information
print(system_info())  # Print system information
print(process_info())  # Print information for the specified process
