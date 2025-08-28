from instagrapi import Client
import time
import os

# Load credentials and target account from environment
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")
TARGET_USERNAME = os.getenv("TARGET_USERNAME")  # 👈 new

# Login
cl = Client()
cl.login(IG_USERNAME, IG_PASSWORD)

# Get target account ID
target_user_id = cl.user_id_from_username(TARGET_USERNAME)

print(f"Monitoring stories from {TARGET_USERNAME}...")

# Keep track of already viewed stories
seen_stories = set()

while True:
    # Get current stories
    stories = cl.user_stories(target_user_id)

    if stories:
        # Filter only new stories
        new_stories = [s for s in stories if s.pk not in seen_stories]

        if new_stories:
            print(f"{TARGET_USERNAME} posted {len(new_stories)} new story/stories!")

            for story in new_stories:
                # Mark story as seen (they will know)
                cl.story_seen([story.pk])
                seen_stories.add(story.pk)
                print(f"Viewed new story {story.pk}")
        else:
            print("No new stories since last check.")
    else:
        print(f"No stories from {TARGET_USERNAME} right now.")

    # Wait before checking again (10 minutes here)
    time.sleep(600)
