# Reddit-BananaLover-Bot

A Reddit bot that encourages banana lovers and discourages banana haters.

## Languages / Frameworks used

* Python
* Heroku (not deployed due to Dyno Hour limitations)

## Purpose / Goals

* Create a bot on Reddit that monitors the 'Bananalovers' subreddit on an interval
* Learn how to complete HTTPS requests in Python
* Improve on regex knowledge
* Improve on JSON interaction in Python

### Dependencies

* praw (Reddit API wrapper)
* pdb
* re
* os
* requests
* json
* threading
* [Insult REST API](https://insult.mattbas.org/api/)

### Installation

* Mac OS X
* Ubuntu
* Windows (if applicable)
* [Python](https://www.python.org/downloads/)
* praw library
* requests library

```python
 pip install praw
 pip install requests
```

### Getting started

* Clone the repository locally
* Create a Reddit account
* Navigate to https://www.reddit.com/prefs/apps/ and obtain your client_id and secret
* Update the praw.ini file with your information. Should be in the Python folder under Lib\Site-Packages\praw\praw.ini. Example settings shown:

![image](https://user-images.githubusercontent.com/14877762/58928700-6aa1fd80-8708-11e9-8eb0-3b7d17cce700.png)

* Make sure that the application name in the brackets is the same as the one set for Reddit app
* Run the script using
```python
python reply_post.py
```


## Usage

* The bot will comment on all posts in the 'BananaLovers' subreddit that contain the phrase "I love ___" (regexes)
* If the blank contains the word "banana", the Bot will encourage the post
* If the blank does not contain the word "banana", the Bot will discourage the post, and insult the user 
* The bot saves all post id's it's commented on to a file so as to not duplicate comments
* The bot has removed all insults including expletives (regexes)

## Demo

#### Bot Encouragement
![image](https://user-images.githubusercontent.com/14877762/58928988-c1f49d80-8709-11e9-8a71-67c60520e34b.png)

#### Bot discouragement
![image](https://user-images.githubusercontent.com/14877762/58929586-8909f800-870c-11e9-91f9-287f47c79ca4.png)

## Team

* Adrian Tran

*Add a "contributors" section if you've incorporated pull requests.*

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/adrianmoo2/reddit-banana-bot/issues/

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:
 
* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!

## Copyright and attribution

Copyright (c) 2019 Adrian Tran. Released under the [MIT License](https://github.com/adrianmoo2/reddit-banana-bot/blob/master/LICENSE).
