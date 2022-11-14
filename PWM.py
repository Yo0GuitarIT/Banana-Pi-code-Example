import RPi.GPIO as gpio
import time

leds = [17, 27, 22]
# led_pwm = list([])

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)

led_pwm = [gpio.PWM(led,60) for led in leds]

[led.start(0) for led in led_pwm]
try:
    while True:
        print("go")
        for i in range(0, 80, 5):
            [led.ChangeDutyCycle(i) for led in led_pwm]
            time.sleep(0.1)
        for i in range(80, 0, -5):
            [led.ChangeDutyCycle(i) for led in led_pwm]
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup(17)
    gpio.cleanup(22)
    gpio.cleanup(27)
