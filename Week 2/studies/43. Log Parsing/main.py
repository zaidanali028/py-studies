import re
import pandas as pd


# todo: send the csv file to myself on telegram every weekday at 7am 

class LogProcessor:
    def __init__(self, log_file_path):
        # Initialize with the path to the log file
        self.log_file_path = log_file_path
        # Initialize an empty list to store cleaned data
        self.cleaned_data = []

    def extract_data(self):
        """
        Extracts necessary information from the log file.
        - Extracts IP addresses, the count of successful requests, 
          and the count of failed requests for each log entry.
        - Adds a row for totals at the end (for successful and failed requests).
        """
        # Define regular expression patterns for IP addresses and request counts
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'  # Matches valid IP addresses
        request_successful_pattern = r'requestsuccessful:\s*(\d+)'  # Matches successful requests count
        request_failed_pattern = r'requestfailed:\s*(\d+)'  # Matches failed requests count

        # Open and read the log file line by line
        with open(self.log_file_path, 'r') as log_file:
            for line in log_file:
                log_data = {}  # Temporary dictionary to store the data for the current line

                # Extract the IP address from the log line
                ip_match = re.search(ip_pattern, line)
                if ip_match:
                    log_data['ip_address'] = ip_match.group(0)

                # Extract the count of successful requests
                successful_match = re.search(request_successful_pattern, line)
                if successful_match:
                    log_data['requestsuccessful'] = int(successful_match.group(1))

                # Extract the count of failed requests
                failed_match = re.search(request_failed_pattern, line)
                if failed_match:
                    log_data['requestfailed'] = int(failed_match.group(1))

                # Append the extracted data to cleaned_data if anything was extracted
                if log_data:
                    self.cleaned_data.append(log_data)
            
            # After reading all the log lines, calculate the totals for requests
            requestfailed_count = sum([data['requestfailed'] for data in self.cleaned_data])
            requestsuccessful_count = sum([data['requestsuccessful'] for data in self.cleaned_data])

            # Create an empty row to maintain structure
            empty_row = {
                'ip_address': '',
                'requestsuccessful': '',
                'requestfailed': ''
            }

            # Create the total row with aggregated values
            total_row = {
                'ip_address': 'TOTAL:',  # Label for the total row
                'requestsuccessful': requestsuccessful_count,  # Total successful requests
                'requestfailed': requestfailed_count  # Total failed requests
            }

            # Add the empty row and total row to the cleaned data
            self.cleaned_data.append(empty_row)
            self.cleaned_data.append(total_row)

    def save_to_csv(self, csv_file_path):
        """
        Saves the extracted and cleaned data into a CSV file.
        Args:
            csv_file_path (str): The path where the CSV file will be saved.
        """
        # Convert cleaned data into a pandas DataFrame
        df = pd.DataFrame(self.cleaned_data)
        
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False)
        
        # Print confirmation that data was saved
        print(f"Data saved to {csv_file_path}")

   
# Usage
log_processor = LogProcessor('serverlogs.log')  # Initialize with the path to the log file
log_processor.extract_data()  # Extract and clean the data from the log file
log_processor.save_to_csv('output.csv')  # Save the cleaned data to a CSV file
