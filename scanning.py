from machine import Pin
import utime

def ultra(trigger, echo, name):
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
       
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   distance = "{:.1f}".format(distance)
   
   print(name+": "+distance + " cm")
   
   return str(distance)



#print("fok")
#ngf = ultra()
#print(ngf)
#while True:
    #ultra(trigger1, echo1, "SENSOR-1")
    #utime.sleep(0.1)
    #ultra(trigger2, echo2, "SENSOR-2")
    #utime.sleep(0.1)
