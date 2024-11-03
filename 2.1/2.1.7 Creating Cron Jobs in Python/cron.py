# GET system info on cron basis
from datetime import datetime  # To work with date and time
import psutil  # To access system and process utilities
import os  # To interact with the operating system

# tracking the status of the cron using grep(grep cron.py /var/log/syslog)
class SystemInfo:
    """
    A class to retrieve and display system information.
    
    TODO:
    1. Create a Python script 
    2. Run `crontab -e` to open the crontab editor
    3. Write the cronjob instruction
    4. Save the crontab file
    5. Run `crontab -l` to confirm your new job instruction
    """

    # Method to retrieve CPU times, including user and system time
    def get_cpu_times(self):
        """Retrieve CPU times, including user and system time."""
        return psutil.cpu_times()
    
    # Method to retrieve current CPU utilization percentage over a specified interval
    def get_cpu_utilization(self, interval=1):
        """Retrieve current CPU utilization percentage over a specified interval."""
        return psutil.cpu_percent(interval=interval)
    
    # Method to get the total number of logical CPU cores in the system
    def get_logical_cores(self):
        """Get the total number of logical CPU cores in the system."""
        return psutil.cpu_count()
    
    # Method to get the total number of physical CPU cores in the system
    def get_physical_cores(self):
        """Get the total number of physical CPU cores in the system."""
        return psutil.cpu_count(logical=False)
    
    # Method to retrieve various CPU statistics like context switches, interrupts, etc.
    def get_cpu_stats(self):
        """Retrieve various CPU statistics like context switches, interrupts, etc."""
        return psutil.cpu_stats()
    
    # Method to retrieve the current CPU frequency information
    def get_cpu_frequency(self):
        """Retrieve the current CPU frequency information."""
        return psutil.cpu_freq()
    
    # Method to get the system load averages for the last 1, 5, and 15 minutes
    def get_load_average(self):
        """Get the system load averages for the last 1, 5, and 15 minutes."""
        return psutil.getloadavg()
    
    # Method to retrieve swap memory usage information
    def get_swap_memory(self):
        """Retrieve swap memory usage information."""
        return psutil.swap_memory()
    
    # Method to retrieve all mounted disk partitions
    def get_disk_partitions(self):
        """Retrieve all mounted disk partitions."""
        return psutil.disk_partitions()
    
    # Method to retrieve disk usage statistics for a specified path
    def get_disk_usage(self, path='/'):
        """Retrieve disk usage statistics for a specified path."""
        return psutil.disk_usage(path)
    
    # Method to retrieve network I/O statistics
    def get_network_io(self):
        """Retrieve network I/O statistics."""
        return psutil.net_io_counters()
    
    # Method to retrieve network connections (TCP, UDP, etc.)
    def get_network_connections(self):
        """Retrieve network connections (TCP, UDP, etc.)."""
        return psutil.net_connections()
    
    # Method to retrieve network interface addresses
    def get_network_interfaces(self):
        """Retrieve network interface addresses."""
        return psutil.net_if_addrs()
    
    # Method to retrieve fan sensor information (if available)
    def get_fan_sensors(self):
        """Retrieve fan sensor information (if available)."""
        return psutil.sensors_fans()
    
    # Method to retrieve battery status and charge information (if applicable)
    def get_battery_status(self):
        """Retrieve battery status and charge information (if applicable)."""
        return psutil.sensors_battery()
    
    # Method to retrieve the system boot time in a human-readable format
    def get_boot_time(self):
        """Retrieve the system boot time in a human-readable format."""
        boot_timestamp = psutil.boot_time()  # Get boot time as seconds since epoch
        return datetime.fromtimestamp(boot_timestamp).strftime("%Y-%m-%d %H:%M:%S")  # Format to readable string
    
    # Method to retrieve information about currently logged-in users
    def get_logged_in_users(self):
        """Retrieve information about currently logged-in users."""
        return psutil.users()

    # Method to write the collected system stats to a specified text file
    def write_stats_to_file(self, filename="system_stats.txt"):
        """Write system statistics to a text file."""
        with open(filename, 'w') as file:  # Open the file in write mode
            # Write header with current timestamp
            file.write(f"System Information Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*50 + "\n\n")  # Separator line
            
            # Write each stat to file with custom formatting
            file.write(f"CPU Times: {self.get_cpu_times()}\n")
            file.write(f"CPU Utilization Percentage: {self.get_cpu_utilization()}\n")
            file.write(f"Number of Logical Cores: {self.get_logical_cores()}\n")
            file.write(f"Number of Physical Cores: {self.get_physical_cores()}\n")
            file.write(f"CPU Statistics: {self.get_cpu_stats()}\n")
            file.write(f"CPU Frequency: {self.get_cpu_frequency()}\n")
            file.write(f"Load Average: {self.get_load_average()}\n")
            file.write(f"Swap Memory Usage: {self.get_swap_memory()}\n")
            file.write(f"Disk Partitions: {self.get_disk_partitions()}\n")
            file.write(f"Disk Usage for '/': {self.get_disk_usage('/')}\n")
            file.write(f"Network I/O Counters: {self.get_network_io()}\n")
            file.write(f"Network Connections: {self.get_network_connections()}\n")
            file.write(f"Network Interface Addresses: {self.get_network_interfaces()}\n")
            file.write(f"Fan Sensors: {self.get_fan_sensors()}\n")
            file.write(f"Battery Status: {self.get_battery_status()}\n")
            file.write(f"System Boot Time: {self.get_boot_time()}\n")
            file.write(f"Logged-in Users: {self.get_logged_in_users()}\n")
            
            file.write("\n" + "="*50 + "\n")  # Footer separator line
            file.write("End of Report\n")  # Indicate end of report
        
        # Confirmation message indicating that the report has been generated
        print(f"System information has been written to {filename}")

# Usage example
info = SystemInfo()  # Create an instance of SystemInfo class
info.write_stats_to_file()  # Call method to write stats to file
