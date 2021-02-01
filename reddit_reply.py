import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')


if not os.path.isfile("posts_replied.txt"):
    posts_replied = []
else:
    with open("posts_replied.txt", "r") as f:
       posts_replied = f.read()
       posts_replied = posts_replied.split("\n")
       posts_replied = list(filter(None, posts_replied))

subreddit = reddit.subreddit("pythonforengineers")
for submission in subreddit.hot(limit=20):
    print(submission.title)
    if re.search("interview", submission.title, re.IGNORECASE) or re.search("coding", submission.title, re.IGNORECASE):
        submission.reply("Practice your Data Structures and Algorithms!!")
        print("bot replied to submission")
        posts_replied.append(submission.id)


with open("posts_replied.txt", "w") as f:
    for post_id in posts_replied:
        f.write(post_id + "\n")
