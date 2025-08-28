# story_watcher.py
import os
from instagrapi import Client

SESSION_FILE = "session.json"
USERNAME = "ganapathi_kodi"   # your account
PASSWORD = "2*4==4*2"         # your password

def main():
    # get target from environment
    target_username = os.getenv("TARGET_USERNAME")
    if not target_username:
        raise ValueError("⚠️ Please set TARGET_USERNAME in environment variables")

    cl = Client()
    cl.load_settings(SESSION_FILE)
    cl.login(USERNAME, PASSWORD)  # uses saved session.json

    # get user id of target
    user_id = cl.user_id_from_username(target_username)

    # fetch stories
    stories = cl.user_stories(user_id)

    if not stories:
        print(f"❌ No active stories for {target_username}")
    else:
        print(f"✅ {target_username} has {len(stories)} active story/stories!")

if __name__ == "__main__":
    main()                print(f"Viewed new story {story.pk}")
        else:
            print("No new stories since last check.")
    else:
        print(f"No stories from {TARGET_USERNAME} right now.")

    # Wait before checking again (10 minutes here)
    time.sleep(600)
