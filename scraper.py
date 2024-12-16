import facebook_scraper as fs
import requests
import json
import browser_cookie3
from http.cookiejar import CookieJar
from facebook_scraper import get_posts
import pandas as pd
def extract_comments(post_id) : 
  true, false = True, False
  cookie_jar = CookieJar ()
  cookies = [
  {
    "domain": ".facebook.com",
    "expirationDate": 1768559399.773692,
    "hostOnly": false,
    "httpOnly": true,
    "name": "sb",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "60_OZMu6ysjnLSs4HLedlXTF",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1734604204,
    "hostOnly": false,
    "httpOnly": false,
    "name": "dpr",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1.25",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1748027747.545204,
    "hostOnly": false,
    "httpOnly": true,
    "name": "ps_n",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1748027747.545273,
    "hostOnly": false,
    "httpOnly": true,
    "name": "ps_l",
    "path": "/",
    "sameSite": "lax",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1760390575.333571,
    "hostOnly": false,
    "httpOnly": true,
    "name": "datr",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "qxXeZrQxv9g2FUpgNe6P7B0T",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1734604204,
    "hostOnly": false,
    "httpOnly": false,
    "name": "wd",
    "path": "/",
    "sameSite": "lax",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1536x695",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1765535399.773609,
    "hostOnly": false,
    "httpOnly": false,
    "name": "c_user",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "61567951333289",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1765535399.773711,
    "hostOnly": false,
    "httpOnly": true,
    "name": "xs",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "42%3AYnBfYkkSUa0qKg%3A2%3A1733999397%3A-1%3A-1",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "expirationDate": 1741775400.01348,
    "hostOnly": false,
    "httpOnly": true,
    "name": "fr",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "1agrPY6ezk5I7Palo.AWXKWVOnZFaj8uxoJ8s94jH7hHo.BnWrsK..AAA.0.0.BnWrso.AWV7uwSIJIo",
    "origin": "https://www.facebook.com"
  },
  {
    "domain": ".facebook.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "presence",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1733999404941%2C%22v%22%3A1%7D",
    "origin": "https://www.facebook.com"
  }
]
  cookies_2  = {"sb":"60_OZMu6ysjnLSs4HLedlXTF","dpr":"1.25","ps_n":"1","ps_l":"1","datr":"qxXeZrQxv9g2FUpgNe6P7B0T","wd":"1366x599","c_user":"61567951333289","fr":"1agrPY6ezk5I7Palo.AWVtu-hJNlJym0FB6G1T48zAUK4.BnWrsK..AAA.0.0.BnWsn7.AWXgW3lNJ0Q","xs":"32%3AMhF5H4W0FXkUTA%3A2%3A1734003195%3A-1%3A-1"}
  for cookie in cookies:
      c = requests.cookies.create_cookie (
      domain=cookie["domain"],name=cookie["name"],
      value=cookie["value"],path=cookie ["path"],
      secure=cookie["secure"], expires=cookie.get("expirationDate"),
      rest={ "HttpOnly": cookie ["httpOnly"], "SameSite": cookie["sameSite"]},)
      cookie_jar.set_cookie(c)
  POST_ID = "pfbid02Zw1m8tg9CmYH8JBqDthBBeyiSGMWmo4qmVK6szUV8s9Vz9kDivW2aycW3P2hgKtLl"

  # number of comments to download -- set this to True to download all comments
  MAX_COMMENTS = 100

  # get the post (this gives a generator)
  gen = fs.get_posts(
      post_urls=["https://www.facebook.com/photo/?fbid=1113949357399418&set=a.631377215656637"],
      options={"comments": MAX_COMMENTS, "progress": True},
      cookies = cookies_2
  )
  post_gen = get_posts("reidandtaylor", pages=10,cookies = cookies_2)
  for post in post_gen : 
     print("the post is ",post)
  print(post_gen)
  print(post_id)
  print(gen)
  # Take the first post
  post = next(gen)
  print(post)
  # Extract comments and get comment_text
  comments = post.get('comments_full', [])
  print(comments)
  comment_texts = [comment['comment_text'] for comment in comments if 'comment_text' in comment]
  return comment_texts

result = extract_comments("3537677729857886")
print(result)