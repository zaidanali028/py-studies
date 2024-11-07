from crontab import CronTab
import getpass

# Get the current user dynamically
user_ = getpass.getuser()

# Create a CronTab instance with the specified user
jobScheduler = CronTab(user_)

# # Check for existing jobs to avoid duplicates
job_command = 'python3 /home/ali/my-Scripts/2.1/2.1.8 Managing Cron Jobs using Python/free.py'
job_exists = False

# # Loop through existing jobs and check for duplicates
for job in jobScheduler:
    if job.command == job_command:
        job_exists = True
        print("Cron job already exists for this command.")
        break

# # If the job does not exist, create a new one
if not job_exists:
    job = jobScheduler.new(command=job_command)
    
    # adding a comment inorder to id this job later
    job.set_comment("Freememory job")
    
#     # Schedule the job to run every 5 minutes
    job.minute.every(5)

#     # Write the job to the crontab
    jobScheduler.write()

    print(f"Cron job added for user {user_} to run every 5 minutes.")

print(user_)