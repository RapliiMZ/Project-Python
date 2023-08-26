import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 23
GPIO_ECHO = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(GPIO_ECHO)== 0:
        start_time = time.time()
    
    while GPIO.input(GPIO_ECHO)== 1:
        stop_time = time.time()
        
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance
if __name__=='__main__':
    try:
        setup()
        while True:
            dist = distance()            
            if dist <= 20:
                print ("ada objek")
            else:
                print("gda objek")
            time.sleep(1)
            
            
    except KeyboardInterrupt:
        GPIO.cleanup()