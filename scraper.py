import facebook_scraper as fs
import requests
import json
from http.cookiejar import CookieJar
from facebook_scraper import get_posts
import pandas as pd
def extract_comments(post_id) : 
  true, false = True, False
  cookie_jar = CookieJar ()
  cookies = [
    {
      "domain": ".facebook.com",
      "expirationDate": 1765492884.865233,
      "hostOnly": false,
      "httpOnly": true,
      "name": "sb",
      "path": "/",
      "sameSite": "no_restriction",
      "secure": true,
      "session": false,
      "storeId": "0",
      "value": "4CHmZiHyeKguI2Ay7v4-NRL7",
      "origin": "https://www.facebook.com"
    },
    {
      "domain": ".facebook.com",
      "expirationDate": 1760917988.059405,
      "hostOnly": false,
      "httpOnly": true,
      "name": "datr",
      "path": "/",
      "sameSite": "no_restriction",
      "secure": true,
      "session": false,
      "storeId": "0",
      "value": "4CHmZjF_ZwE0KbKs3n61hE0e",
      "origin": "https://www.facebook.com"
    },
    {
      "domain": ".facebook.com",
      "expirationDate": 1760918048.639864,
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
      "expirationDate": 1760918048.639954,
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
      "expirationDate": 1731537690,
      "hostOnly": false,
      "httpOnly": false,
      "name": "wd",
      "path": "/",
      "sameSite": "lax",
      "secure": true,
      "session": false,
      "storeId": "0",
      "value": "1528x738",
      "origin": "https://www.facebook.com"
    },
    {
      "domain": ".facebook.com",
      "expirationDate": 1731537690,
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
      "expirationDate": 1762468884.865126,
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
      "expirationDate": 1762468884.865253,
      "hostOnly": false,
      "httpOnly": true,
      "name": "xs",
      "path": "/",
      "sameSite": "no_restriction",
      "secure": true,
      "session": false,
      "storeId": "0",
      "value": "12%3AuP6Rke5s5E1zUA%3A2%3A1730932881%3A-1%3A-1",
      "origin": "https://www.facebook.com"
    },
    {
      "domain": ".facebook.com",
      "expirationDate": 1738708885.141322,
      "hostOnly": false,
      "httpOnly": true,
      "name": "fr",
      "path": "/",
      "sameSite": "no_restriction",
      "secure": true,
      "session": false,
      "storeId": "0",
      "value": "1RFoEolQ0v3QuLZpv.AWXzY_4g66BKfX-K5TpixArVVUY.BnJ_Zf..AAA.0.0.BnK_CU.AWVdQ6sd2aw",
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
      "value": "C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1730932890967%2C%22v%22%3A1%7D",
      "origin": "https://www.facebook.com"
    }
  ]
  for cookie in cookies:
      c = requests.cookies.create_cookie (
      domain=cookie["domain"],name=cookie["name"],
      value=cookie["value"],path=cookie ["path"],
      secure=cookie["secure"], expires=cookie.get("expirationDate"),
      rest={ "HttpOnly": cookie ["httpOnly"], "SameSite": cookie["sameSite"]},)
      cookie_jar.set_cookie(c)
  POST_ID = "pfbid0TTRfUg1jkL7gJC8faEQrGDLVKQfsu8rSJsh1FNZqDw5wy4vJ7u49YCye5odrxLVil"

  # number of comments to download -- set this to True to download all comments
  MAX_COMMENTS = 100

  # get the post (this gives a generator)
  gen = fs.get_posts(
      post_urls=[POST_ID],
      options={"comments": MAX_COMMENTS, "progress": True}
  )

  # Take the first post
  post = next(gen)

  # Extract comments and get comment_text
  comments = post.get('comments_full', [])
  comment_texts = [comment['comment_text'] for comment in comments if 'comment_text' in comment]
  return comment_texts