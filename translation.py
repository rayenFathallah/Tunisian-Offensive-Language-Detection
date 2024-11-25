import pandas as pd
import numpy as np
import json
import requests
from deep_translator import GoogleTranslator
from langdetect import detect
import re
def LAT2AR(word):
  path = "https://api.yamli.com/transliterate.ashx?word={}&tool=api&account_id=000006&prot=https:&hostname=www.yamli.com&path=/&build=5515".format(word)
  response = requests.get(path)
  html = response.content
  try:
    newWord = json.loads(html.decode("utf-8"))["r"].split("|")[0].rsplit('/',1)[0]
  except:
    return word
  return (word if newWord == ""  else newWord)

def translate(text):
  try :
    newtext = []
    text = re.sub(r"[,.;@/#?\!&$]+\ *", " ", text)
    text = text.split(' ')
    blist = [1 if (len(txt)>1 and detect(txt) in['fr','en']) else 0 for txt in text]
    try:
      for i in range(len(blist)):
        if blist[i] == 1:
          newtext.append(GoogleTranslator(source='auto', target='ar').translate(text[i]))
        else:
          newtext.append(LAT2AR(text[i].strip()))
    except:
      print(text[i])
      newtext.append(LAT2AR(text[i].strip()))

    return ' '.join(newtext)
  except:
    return " "