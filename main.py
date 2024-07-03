import scanning
from machine import Pin
import utime
import _thread

# Initialize hardware, pin numbers may change

# Ultrasound Sensor 1
trigger1 = Pin(21, Pin.OUT)
echo1 = Pin(20, Pin.IN)

# Ultrasound Sensor 2
trigger2 = Pin(3,Pin.OUT)
echo2 = Pin(2, Pin.IN)

# RED Led - will use it for debugging, if user EXITED
red_led = Pin(15,Pin.OUT)

# GREEN Led - will use it for debugging, if user ENTERED
green_led = Pin(14,Pin.OUT)

# We create a semaphore (A.K.A lock)
mutex = _thread.allocate_lock()
triggered = {"status": False}  # Use a dict to allow mutability
# Just setting an average default distance for each sensor
def set_average_distance():
    average_distance_1 = 0.0
    average_distance_2 = 0.0
    iterations = 100
    for i in range(iterations):
        average_distance_1 += float(scanning.ultra(trigger1, echo1, "SENSOR-1"))
        utime.sleep(0.2)
        average_distance_2 += float(scanning.ultra(trigger2, echo2, "SENSOR-2"))
        utime.sleep(0.2)
        
    average_distance_1 = average_distance_1 / iterations
    average_distance_2 = average_distance_2 / iterations
    
    return [average_distance_1, average_distance_2]

def thread_func(triggered):
    while True:
        mutex.acquire()
        utime.sleep(0.3)
        red_led.value(0)
        dist = float(scanning.ultra(trigger1, echo1, "SENSOR-1"))
        if dist <= 0.5 * avg_1:
            #print("triggered SENSOR-1 with distance: " + str(dist))
            #print("Trigger status is: " + str(triggered["status"]))
            if triggered["status"]:
                print("EXITED")
                red_led.value(1)
                #utime.sleep(1)
                triggered["status"] = False
            else:
                triggered["status"] = True
                mutex.release()
                utime.sleep(2)
                triggered["status"] = False
                continue
        mutex.release()

avg_1, avg_2 = set_average_distance()

print(avg_1)
print(avg_2)

_thread.start_new_thread(thread_func, (triggered,))

def main():
    while True:
        mutex.acquire()
        utime.sleep(0.3)
        green_led.value(0)
        dist = float(scanning.ultra(trigger2, echo2, "SENSOR-2"))
        if dist <= 0.5 * avg_2:
            if triggered["status"]:
                print("ENTERED")
                green_led.value(1)
                #utime.sleep(1)
                triggered["status"] = False
            else:
                triggered["status"] = True
                mutex.release()
                utime.sleep(2)
                triggered["status"] = False
                continue
        mutex.release()

# Start the main function
main()
