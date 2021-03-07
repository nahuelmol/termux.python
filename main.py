from pimux import function, Sensors

v = function.misc()
s = Sensors.sensor()

v.vibrate()

v.brightness(Brightness=100)
v.brightness(Brightness=25)

sensors_resulted = s.listSensor()
print(sensors_resulted)