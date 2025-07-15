import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="PersonaScraper by /u/fcuktony"
)

def scrape_user(username, limit=50):
    try:
        user = reddit.redditor(username)
        # Make a dummy call to raise NotFound if the user doesn't exist
        _ = user.id
    except NotFound:
        raise ValueError(f"User '{username}' not found on Reddit.")

    data = []

    try:
        for comment in user.comments.new(limit=limit):
            data.append({
                "type": "comment",
                "content": comment.body,
                "permalink": f"https://reddit.com{comment.permalink}"
            })

        for submission in user.submissions.new(limit=limit):
            data.append({
                "type": "post",
                "content": submission.title + "\n" + submission.selftext,
                "permalink": f"https://reddit.com{submission.permalink}"
            })

    except Exception as e:
        raise RuntimeError(f"Error while fetching data: {str(e)}")

    return data