import requests

# GitHub repo details
OWNER = "torvalds"
REPO = "linux"

# GitHub API URL
url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"

# Fetch the commit data
response = requests.get(url)
if response.status_code == 200:
    commits = response.json()
    for commit in commits[:5]:  # Limiting to 5 commits for brevity
        author = commit["commit"]["author"]["name"]
        message = commit["commit"]["message"]
        print(f"Author: {author}\nMessage: {message}\n{'-'*40}")
else:
    print("Failed to fetch commits:", response.status_code)
