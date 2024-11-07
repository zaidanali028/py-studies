import requests

# Define the URL and parameters
url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId': 1}

# Make the request with error handling
try:
    # Check if the URL is not empty
    if not url:
        raise ValueError("The URL is empty.")
    
    # Send a GET request
    response = requests.get(url, params=params)
    
    # Check if the response status is OK (status code 200)
    if response.status_code == 200:
        print("Request successful:", response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error with the request:", e)
except ValueError as ve:
    print("Value error:", ve)
except Exception as ex:
    print("An unexpected error occurred:", ex)
