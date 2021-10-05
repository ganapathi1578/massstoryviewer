import instabot
from instabot import Bot
import time
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

HASHTAGS = ['fashion', 'style', "model", "shopping", "dress"]
SLEEP_TIME_BETWEEN_MAIN_LOOP = 0
SLEEP_TIME_BETWEEN_HASHTAG_LOOP = 0
USERNAME = "black_editz36"
PASSWORD = "9133775273g"

bot = instabot.Bot()

bot.login(username=USERNAME, password=PASSWORD)

# MAIN LOOP
while True:
    try:
        for hashtag in HASHTAGS :
            clear()
            # GET USERS FROM HASHTAG
            users = bot.get_hashtag_users(hashtag)
            for id in users:
                # WATCH USER STORIES
                if bot.watch_users_reels(id):
                    bot.logger.info(f'Instagram user: {id}, Total stories viewed: {bot.total["stories_viewed"]}')
            bot.logger.info(f'Sleeping for {SLEEP_TIME_BETWEEN_HASHTAG_LOOP} seconds...')           
            time.sleep(SLEEP_TIME_BETWEEN_HASHTAG_LOOP)
        bot.logger.info(f'Sleeping for {SLEEP_TIME_BETWEEN_MAIN_LOOP} seconds...')           
        time.sleep(SLEEP_TIME_BETWEEN_MAIN_LOOP)

    except Exception as e:
        bot.logger.info(e)
        time.sleep(SLEEP_TIME_BETWEEN_MAIN_LOOP)