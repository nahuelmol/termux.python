import pimux
from termux import API
import requests
#from commands import index
#from info import index

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

API.vibrate()


