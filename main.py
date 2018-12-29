import os
import tweepy
from dotenv import load_dotenv

load_dotenv(".env")


# 環境変数取得
ck = os.environ["ck"]
cs = os.environ["cs"]
tk = os.environ["tk"]
ts = os.environ["ts"]

# 認証
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(tk, ts)
api = tweepy.API(auth)

for t in tweepy.Cursor(api.favorites, screen_name="tayo1325", count=200).items():
    if hasattr(t, "extended_entities"):
        for m in t.extended_entities["media"]:
            if m["type"] == "photo":
                print(m["media_url_https"])
