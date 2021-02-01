import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")