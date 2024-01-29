import schedule
import time
from github import Github

def create_issue(repo_name, title, body):
    g = Github("YOUR_PERSONAL_ACCESS_TOKEN")
    repo = g.get_user().get_repo(repo_name)
    repo.create_issue(title=title, body=body)

def job():
    # Define your issue creation logic here
    create_issue("your-repo", "Issue Title", "Issue Body")

# Schedule the job every day (you can modify this as needed)
schedule.every().day.at("10:00").do(job)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
