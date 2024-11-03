import psutil  # Import the psutil library to access system and process utilities
from datetime import datetime

# Retrieve and print CPU times, which includes user and system CPU time
print("CPU Times:", psutil.cpu_times())

# Retrieve and print the current CPU utilization percentage over a 1-second interval
print("CPU Utilization Percentage:", psutil.cpu_percent(1))

# Print the total number of logical CPU cores in the system
print("Number of logical cores in system:", psutil.cpu_count())

# Print the total number of physical CPU cores in the system
print("Number of physical cores in system:", psutil.cpu_count(logical=False))

# Retrieve and print various CPU statistics such as context switches, interrupts, etc.
print("CPU Statistics:", psutil.cpu_stats())

# Retrieve and print the current CPU frequency (speed) information
print("CPU Frequency:", psutil.cpu_freq())

# Retrieve and print the system load averages for the last 1, 5, and 15 minutes
print("Load Average:", psutil.getloadavg())

# Retrieve and print information about swap memory usage
print("Swap Memory Usage:", psutil.swap_memory())

# Retrieve and print a list of all mounted disk partitions
print("Disk Partitions:", psutil.disk_partitions())

# Retrieve and print the disk usage statistics for the root directory
print("Disk Usage for '/':", psutil.disk_usage('/'))

# Retrieve and print network I/O statistics (bytes sent/received)
print("Network I/O Counters:", psutil.net_io_counters())

# Retrieve and print network connections (TCP, UDP, etc.)
print("Network Connections:", psutil.net_connections())

# Retrieve and print the addresses of the network interfaces
print("Network Interface Addresses:", psutil.net_if_addrs())

# Retrieve and print fan sensor information (if available)
print("Fan Sensors:", psutil.sensors_fans())

# Retrieve and print battery status and charge information (if applicable)
print("Battery Status:", psutil.sensors_battery())

# Retrieve and print the system boot time in a human-readable format
boot_time = psutil.boot_time()  # Get boot time in seconds since epoch
print("System Boot Time (Unix Timestamp):", boot_time)

# Convert the boot time to a readable format
boot_time_readable = datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")
print("System Boot Time (Readable Format):", boot_time_readable)

# Retrieve and print information about currently logged-in users
print("Logged-in Users:", psutil.users())
