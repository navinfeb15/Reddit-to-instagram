import os
import praw
import logging
import pandas as pd
import urllib.request
from datetime import datetime as dt


df = None


def log_in():
    reddit = praw.Reddit(
        client_id="your client_id",
        client_secret="your client_secret",
        password="your password",
        user_agent="testscript by u/username",
        username="your username",
    )

    subreddit = reddit.subreddit("dankmemes")

    global url, df
    df = pd.DataFrame()

    titles = []
    scores = []
    ids = []
    url = []

    for submission in subreddit.hot(limit=20):
        titles.append(submission.title)
        scores.append(submission.score)
        ids.append(submission.id)
        url.append(submission.url)

    df["Title"] = titles
    df["Id"] = ids
    df["Upvotes"] = scores  # upvotes
    df["url"] = url
    df["Date"] = dt.now().strftime("%c")

    return df


def down_imgs():
    try:

        # Check imgs/logs folder exixts, if not create ...
        if "imgs" in os.getcwd():
            os.chdir("..")
        if not os.path.isdir("imgs"):
            os.makedirs("./imgs")
        if not os.path.isdir("logs"):
            os.makedirs("./logs")

        os.chdir("imgs")

        logging.basicConfig(
            filename="../logs/full_log",
            format="%(asctime)s %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            level=logging.ERROR,
        )
        img_log = []
        for i in range(0, len(url)):
            link = url[i]

            # Get the link of the submission
            s_url = str(link)

            # Check if the link is an image
            if (
                s_url.endswith("jpg")
                or s_url.endswith("jpeg")
                or s_url.endswith("png")
                or s_url.endswith("gif")
            ):

                # Retrieve the image and save it in current folder
                file_name = s_url.split("/")[-1]
                file_id = df[df["url"].str.contains(file_name)]["Id"].iloc[0]
                img_log.append(file_id)
                urllib.request.urlretrieve(link, file_name)
                print("Dounloaded file - ", file_name)

        logging.info(img_log)
        output_path = "../logs/log.csv"
        df.to_csv(
            output_path, mode="a+", index=False, header=not os.path.exists(output_path)
        )
    except Exception as e:
        print("error during downloading : ", e)
