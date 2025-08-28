from instagrapi import Client
import time

# Login to your account
cl = Client()
cl.login("your_username", "your_password")

# The account you want to monitor
target_username = "friend_username"
target_user_id = cl.user_id_from_username(target_username)

print(f"Monitoring stories from {target_username}...")

# Keep track of already viewed stories
seen_stories = set()

while True:
    # Get current stories
    stories = cl.user_stories(target_user_id)

    if stories:
        # Filter only new stories
        new_stories = [s for s in stories if s.pk not in seen_stories]

        if new_stories:
            print(f"{target_username} posted {len(new_stories)} new story/stories!")

            for story in new_stories:
                # Mark story as seen (they will know)
                cl.story_seen([story.pk])
                seen_stories.add(story.pk)
                print(f"Viewed new story {story.pk}")
        else:
            print("No new stories since last check.")
    else:
        print(f"No stories from {target_username} right now.")

    # Wait before checking again (10 minutes here)
    time.sleep(600)
