import os
import time
import shutil
import instabot
import pandas as pd


def readcsv():
    global tags
    global filecsv
    if "imgs" in os.getcwd():
        os.chdir("..")
        filecsv = pd.read_csv("logs/log.csv")
        with open("tags.txt", "r") as tagfile:
            tags = tagfile.readlines()
        os.chdir("imgs")
    else:
        filecsv = pd.read_csv("logs/log.csv")
        with open("tags.txt", "r") as tagfile:
            tags = tagfile.readlines()


def clean_up():
    try:
        if "imgs" in os.getcwd():
            os.chdir("..")
        dir = "config"
        # checking whether config folder exists or not
        if os.path.exists(dir):
            try:
                # removing it because it makes problems with new uploads
                shutil.rmtree(dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
            os.chdir("imgs")

    except Exception as e:
        print("Errror during cleaning upp : ", e)
        pass


def use_caption(fname):
    caption = filecsv[filecsv["url"].str.contains(fname)].Title.astype("string").iloc[0]
    caption = caption + str("".join(tags))
    return caption


def upload_post():

    clean_up()
    if "imgs" not in os.getcwd():
        os.chdir("imgs")
    bot = instabot.Bot()
    bot.login(username="your_username", password="your_password")
    time.sleep(10)

    try:

        for file in os.listdir():
            if not file.endswith("REMOVE_ME"):
                f_title = file.split(".")[0]
                if file.endswith(".jpeg"):
                    bot.upload_photo(file, caption=use_caption(f_title))
                elif file.endswith(".mp4"):
                    bot.upload_video(file, caption=use_caption(f_title))
                print("sleeping for 6 minutes")
                # sleep after posting for 5 minutes so not to spam API
                time.sleep(6 * 60)

    except Exception as e:
        print("Error while uploading post: ", e)
