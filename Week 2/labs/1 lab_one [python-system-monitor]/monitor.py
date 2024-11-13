import os
import time
from mailjet_rest import Client
import psutil

# Set up Mailjet credentials as environment variables for added security
api_key = os.getenv('MAIL_JET_API_KEY')
api_secret = os.getenv('MAIL_JET_API_SECRET')

def send_alert(subject, message):
    """Sends an alert email with the specified subject and message."""
    if not api_key or not api_secret:
        print("Mailjet API credentials are missing. Please set MAIL_JET_API_KEY and MAIL_JET_API_SECRET as environment variables.")
        return

    try:
        # Instantiate the Mailjet client
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Define the email data
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": os.getenv("SYSTEM_EMAIL", "system@example.com"),
                        "Name": "24/7 SysMon"
                    },
                    "To": [
                        {
                            "Email": os.getenv("ADMIN_EMAIL", "zaidanali028@gmail.com"),
                            "Name": "Admin"
                        }
                    ],
                    "Subject": subject,
                    "HTMLPart": f"<h3>{message}</h3>"
                }
            ]
        }

        # Send the email and check the response
        result = mailjet.send.create(data=data)
        if result.status_code == 200:
            print(f"Email sent successfully: {result.status_code}")
        else:
            print(f"Failed to send email: Status Code {result.status_code}, {result.json()}")

    except Exception as e:
        print(f"Error occurred while sending email: {str(e)}")

# Define system time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# Define System thresholds
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

# Check system metrics
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Create alert message based on threshold breaches
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

# Trigger email alert if any threshold is breached
if alert_message:
    send_alert(f"Python Monitoring Alert - {formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")
