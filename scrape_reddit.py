import praw

reddit = praw.Reddit('bananabot')

subreddit = reddit.subreddit('BananaLovers')

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------\n")