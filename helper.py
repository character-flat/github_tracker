import requests
class GithubActivity:
    def __init__(self, username):
        self.username = username
        self.request_url = f"https://api.github.com/users/{username}/events"
        self.activity = None

    def get_user_activity(self):
        response = requests.get(self.request_url)
        if response.status_code == 404:
            print(f"API Failed with status code 404 for user {self.username}")
            return False
        return response.json()

    def print_user_activity(self):
        if self.activity is None:
            self.activity = self.get_user_activity()
        if not self.activity:
            print(f"User {self.username} not found")
            return
        if self.activity == []:
            print(f"No activity found for {self.username}")
            return
        for event in self.activity:
            if event['type'] == 'PushEvent':
                print(f"Pushed {len(event['payload']['commits'])} commits to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"Opened a new issue in {event['repo']['name']}")
            elif event['type'] == 'WatchEvent':
                print(f"Starred {event['repo']['name']}")
            else:
                print(f"{event['type']} event on {event['repo']['name']}")


