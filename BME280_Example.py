import BME280

sensor = BME280.BME280()

degrees = sensor.read_temperatureC()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
print 'Humidity  = {0:0.2f} %'.format(humidity)
