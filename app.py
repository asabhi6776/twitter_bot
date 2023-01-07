import tweepy
import datetime

# Set up your API keys and secrets
consumer_key = "paste here"
consumer_secret = "paste here"
access_token = "paste here"
access_token_secret = "paste here"

# Authenticate your app and create an API client
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def get_day_of_week():
  # Get the current date
  today = datetime.date.today()

  # Format the date as the name of the day of the week
  return today.strftime("%A")

def post_tweet():
  # Get the current day of the week
  day = get_day_of_week()

  # Post a tweet with the message "Today is day [day of the week]"
  api.update_status(f"Today is {day}")

# Run the bot
post_tweet()
