
# Flask Blog Application


# Instagram Bot

This is a Python script that automates uploading images and videos to Instagram using the Instabot library. It also includes functionality to convert images to a square format, change file extensions, and download images from Reddit for Instagram posts.

## Prerequisites

- Python 3.x
- Required Python packages: instabot, pandas, Pillow, moviepy, praw, urllib

## Installation

1. Clone the repository:


```
git clone  [https://github.com/your_username/instagram-bot.git](https://github.com/your_username/instagram-bot.git)
```

2. Install the required Python packages:


```
pip install instabot pandas Pillow moviepy praw
```

## Configuration

Before running the script, you need to provide the following configuration:

1. Instagram Account:
   - Set your Instagram username and password in the `upload_post()` function.
   - Make sure to enable two-factor authentication if applicable.

2. Reddit Account:
   - Set your Reddit API credentials (client_id, client_secret, password, user_agent, username) in the `log_in()` function.

## Usage

1. Prepare your images and videos:
   - Place the images and videos you want to upload in the `imgs` folder.
   - Supported formats: JPEG, PNG, GIF (for videos, please ensure they are in a supported format).

2. Run the script:


```
python process.py
```

3. The script will perform the following tasks:
   - Convert images to a square format.
   - Change file extensions to JPEG for compatibility with Instagram.
   - Download images from Reddit using the provided credentials.
   - Upload the processed images and videos to your Instagram account.

## Important Notes

- Please use this script responsibly and in compliance with Instagram's terms of service.
- Be aware of Instagram's rate limits to avoid being blocked or banned.
- It is recommended to run the script on a dedicated account, separate from your personal Instagram account.

