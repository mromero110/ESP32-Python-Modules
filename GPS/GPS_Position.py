from machine import UART, Pin, SPI,I2C
from micropyGPS import MicropyGPS
import utime
import nmea

uart = UART(2, 9600)
now = utime.ticks_ms()
my_nmea = nmea.nmea(debug=1)

#while 1:
class GetLocation():
    def Tracking_GPS():
        while uart.any():
            b = uart.read()
            my_nmea.parse(b)
#Si el incremento de precisión en milisegundos aumenta en x valor, entonces restablecerá la variable now
#Esto para mostrar datos veridicos:
        if utime.ticks_diff(utime.ticks_ms(), now) > 5000:
            now = utime.ticks_ms()
            global lat
            lat = my_nmea.latitude
            global long
            long = my_nmea.longitude
            print("Lat:{}".format(my_nmea.latitude))
            print("Lon:{}".format(my_nmea.longitude))
            utime.sleep(3)
#Geolocalization=GetLocation
#Geolocalization.Tracking_GPS()