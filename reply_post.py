import praw
import pdb
import re
import os
import requests
import json
import threading

def jdump(json_obj):
    return json.dumps(json_obj.json()['insult'])

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

def replyPost():
    reddit = praw.Reddit('bananabot')

    subreddit = reddit.subreddit('BananaLovers')

    for submission in subreddit.hot(limit=5):
        if submission.id not in posts_replied_to:
            if re.search("i love bananas", submission.title, re.IGNORECASE):
                submission.reply("Adrian says, \"ME TOO!!\"")
                print("Bot replied to: ", submission.title)
                posts_replied_to.append(submission.id)
            elif re.search('I love (?!banana(s)*).+', submission.title, re.IGNORECASE):
                response = requests.get('https://insult.mattbas.org/api/insult.json',
                        params = {'who':  submission.author}
                )
                json_dump = jdump(response)

                while re.search('fuck|shit|ass|piss', json_dump, re.IGNORECASE):
                    response = requests.get('https://insult.mattbas.org/api/insult.json',
                        params = {'who':  submission.author}
                    )
                    json_dump = jdump(response)
                
                submission.reply("Adrian says, \"Are you kidding me?! Bananas are way better!!\"\n\n\nAlso, " + json_dump.replace('"', ''))
                posts_replied_to.append(submission.id)

set_interval(replyPost, 30)

with open("posts_replied_to", "w") as f:
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


