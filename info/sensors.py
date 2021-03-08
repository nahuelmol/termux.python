from pimux import Sensors

def returner(s):
  sensors_resulted = s.listSensor()
  sensors = eval(sensors_resulted)

  list_sensors = sensors.get('sensors')
    
  return list_sensors
