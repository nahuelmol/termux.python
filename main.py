from pimux import function
import json

import requests
#from commands import index
#from info import index

wifi = function.wifi()
camera = function.camera()
volume = function.volume()
tts = function.tts()

x = requests.get('https://w3schools.com/python/demopage.htm')


wifi_info = json.loads(wifi.connectInfo())
ip_address = wifi_info.get('ip')
mac_address = wifi_info.get('mac_address')
link_speed = wifi_info.get('link_speed_mbps')
#camera.takephoto(cid=1,saveas='new_.jpg')
volume_info = volume.volumeInfo()
tts_info = tts.ttsinfo()

#help(function)
print("ip address: {}\n\
mac_address: {}\n\
link_speed: {}".format(ip_address,mac_address, link_speed))



