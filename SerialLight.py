import RPi.GPIO as gpio
import time
led1 = 17
led2 = 27
led3 = 22

gpio.setmode(gpio.BCM)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)

try:

    while True:
        gpio.output(led1 , 1)
        time.sleep(0.5)
        gpio.output(led1 , 0)
        time.sleep(0.5)
        gpio.output(led2 , 1)
        time.sleep(0.5)
        gpio.output(led2, 0)
        time.sleep(0.5)
        gpio.output(led3 , 1)
        time.sleep(0.5)
        gpio.output(led3 , 0)
        time.sleep(0.5)
finally:
    gpio.cleanup(22)
    gpio.cleanup(17)
    gpio.cleanup(27)
    print('off')
