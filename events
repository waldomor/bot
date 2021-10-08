import time
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

req = Request("https://www.facebook.com/pg/esnromaase/events/?ref=page_internal", headers={'': ''})
webpage = urlopen(req, timeout=10)
b4 = BeautifulSoup(webpage, "html.parser")
events_list = b4.find_all('div', id="upcoming_events_card")

for allContainers in events_list:
    eventName = allContainers.find('span').getText()
#get.('span')
printed = []
print(eventName)
while True:
    if eventName not in printed:
        requests.get("https://api.telegram.org/bot{"XXXXXXXXXXXX"}/sendMessage?chat_id={"-1591353291"}&text={}".format(eventName))
        time.sleep(10)
        printed.append(eventName)
