import BME280

sensor = BME280.BME280()

degreesC = sensor.read_temperatureC()
degreesF = sensor.read_temperatureF()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

print 'Temp      = {0:0.3f} deg C'.format(degreesC)
print 'Temp      = {0:0.3f} deg F'.format(degreesF)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
print 'Humidity  = {0:0.2f} %'.format(humidity)
