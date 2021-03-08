from pimux import function, Sensors

v = function.misc()
s = Sensors.sensor()

#if __name__ == '__main__':
vib_d = 250

v.vibrate(duration = vib_d)
v.brightness(Brightness=100)
v.brightness(Brightness=25)
v.vibrate(duration = vib_d)