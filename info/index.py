from pimux import Sensors
from info.sensors import returner



def sensors_sending(my_sensor,listed):
  sensor1 = "LIS2DS Accelerometer"
  sensor3 = "LIS2DS Significant Motion Detector"
  sensor4 = "LIS2DS Tilt Detector"
  sensor2 = "STK3013 Proximity"
  sensor5 = "Screen Orientation Sensor"

  allsensors = [
    sensor1,sensor2,
    sensor3,sensor4,
    sensor5
  ]
  
  if allsensors == listed:
    sensor_response = my_sensor.specificSensors(sensor5)


if __name__ == 'info.index':
  my_sensor = Sensors.sensor()
  listed = returner(my_sensor)
  sensors_sending(my_sensor, listed)