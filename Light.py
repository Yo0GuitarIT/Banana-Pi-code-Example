import RPi.GPIO as GPIO

LED_PIN = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
 
try:
    print(' Ctrl-C to Off light \n')
    GPIO.output(LED_PIN, GPIO.HIGH)
    while True:
        next
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup(17)
    print('off')
