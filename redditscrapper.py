
import praw
#import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="MEfhqBwSNfSNFLYAXpU2cA",         # your client id
                               client_secret="89uwluR4NKy65kGk5aD4im97TMq68A",      # your client secret
                               user_agent="")        # your user agent
 

subreddit = reddit_read_only.subreddit("nba")
 
for post in subreddit.hot(limit=5):
    print(post.title)
    print()