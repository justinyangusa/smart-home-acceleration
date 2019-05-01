import RPi.GPIO as GPIO
import time

"""
    Ultrasonic Main function. Calls init, and then loops forever.
    Might need modifications to update the flag variable
"""
def ultrasonic(flag):
    TRIG, ECHO = ultrasonic_init()

    # Modify these conditions to update flag variable correctly
    while True:
        dist = get_distance(TRIG, ECHO)
        flag = is_close(dist)   # Set flag
        time.sleep(0.2)

    ultrasonic_done()



def ultrasonic_init():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    # time.sleep(2)
    return TRIG, ECHO

def get_distance(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.01)    # 10ms
    GPIO.output(TRIG, False)

    while (GPIO.input(ECHO) == 0):
        # No response so just wait and do nothing
        # start = time.time()
    start = time.time()
    while (GPIO.input(ECHO) == 1):
        # Just wait and time the signal
        # end = time.time()
    end = time.time()

    t = end - start
    distance = t * 17150    # 343 m/s -> 171.5 m/s
    distance = int(distance) # round
    print("Distance:", distance,"cm")

    return distance

def is_close(distance):
    if (distance < 120):
        return True
    else:
        return False

def ultrasonic_done():
    GPIO.cleanup()
