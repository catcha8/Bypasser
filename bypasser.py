import os

try:
  import requests
except:  
  os.system("pip install requests")

try:
  import pystyle
except:  
  os.system("pip install pystyle")

from requests import *
from pystyle import *

bypasslink = Write.Input("Input the url to bypass: ", Colors.purple_to_red, interval=0)

data = {
  "url": bypasslink,
}

r = post("https://api.bypass.vip/", data=data)
result_data = r.json()

if result_data['success'] == True:
    Write.Print(f"\n\nWebsite Found: {result_data['website']}\n\n", Colors.blue_to_green, interval=0)
    Write.Print(f"Old: {bypasslink} \nBypassed link:{result_data['destination']}\n", Colors.green, interval=0)
    Write.Print(f"Bypassed In: {result_data['time_ms']}ms\n\n", Colors.blue, interval=0)
    r = get(result_data['destination'])
    Write.Print(f"Result Data: {r.text}\n\n", Colors.green, interval=0)
else:
    Write.Print(f"An error has occured or this link is invalid !\n\n", Colors.red, interval=0)


input()
