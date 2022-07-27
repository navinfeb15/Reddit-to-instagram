# Reddit to Instagram

**Reddit-to-Instagram** allows you to get hot/top/new/rising posts from various subreddits and repost them to your Instagram account automatically. This bot calls a python script that uses PRAW API to get posts from a subreddit of your choice. It automatically filters out duplicates on multiple calls, resizes the image for Instagram standards, post the picture with the title as caption.

## This script will do the following:

-   Download images from a given subreddit
    
-   Store Title, Username and downloaded image path in a Dataframe file
    
-   Process Images and videos to fit expected Ratio (1:1)
    
-   Upload each of images to Instagram. Captions can be edited in **tags.txt** file

## To Run This File:
-   Clone or download this repo.

-   Create a Reddit app from  [here](https://ssl.reddit.com/prefs/apps/).
-   Install requirements by typing  `pip install -r requirements.txt`
-   Edit the rscrapy and insatbot file.
-   Run  `process.py`
