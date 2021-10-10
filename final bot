import time
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import pandas as pd
url = 'https://raw.githubusercontent.com/waldomor/telegram/main/qna_chitchat_esnromaase33.tsv'

 
df = pd.read_csv(url, sep="\t")


#base_url = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#base_url = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
base_url = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxx"


def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  print(data)

  for result in data["result"]:
    send_msg(result)
  
  if data["result"]:
    return data["result"][-1]["update_id"] + 1



def auto_answer(message):
  answer = df.loc[df['Question'].str.lower() == message.lower()]  

  if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer


def send_msg(message):
  text = message["message"]["text"]
  message_id = message["message"]["message_id"]
  answer = auto_answer(text)

  parameters = {
      "chat_id" : "-562917794",
      "text" : answer,
      "reply_to_message_id" : message_id
  }

  resp = requests.get(base_url + "/sendMessage", data = parameters)
  print=(resp.text)

offset = 0

while True:  
