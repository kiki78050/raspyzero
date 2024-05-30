import RPi.GPIO as GPIO
import time

PWM_GPIO = 18
duty_cycle = 60

GPIO.setmodde(GPIO.BCM)
GPIO.setup(PWM_GPIO, GPIO.OUT)

pwm = GPIO.PWM(PWM_GPIO, 50)
pwm.start(0)

pwm.ChangeDutyCycle(duty_cycle)