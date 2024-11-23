import sys
from helper import GithubActivity

if len(sys.argv) < 2:
    print("Usage: task-cli <command> [<args>]")
    sys.exit(1)

username = sys.argv[1]

activity = GithubActivity(username)

activity.print_user_activity()




