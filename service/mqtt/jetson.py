import Jetson.GPIO as GPIO

OPEN_PIN = 38
CLOSE_PIN = 37
SOUND_PIN = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OPEN_PIN, GPIO.OUT)
GPIO.setup(CLOSE_PIN, GPIO.OUT)
GPIO.setup(SOUND_PIN, GPIO.OUT)

def open():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(OPEN_PIN, GPIO.OUT)
    GPIO.setup(CLOSE_PIN, GPIO.OUT)
    GPIO.setup(SOUND_PIN, GPIO.OUT)

    GPIO.output(OPEN_PIN, GPIO.HIGH)
    GPIO.output(SOUND_PIN, GPIO.LOW)
    GPIO.output(CLOSE_PIN, GPIO.LOW)

def close():
    clear()
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(OPEN_PIN, GPIO.OUT)
    GPIO.setup(CLOSE_PIN, GPIO.OUT)
    GPIO.setup(SOUND_PIN, GPIO.OUT)

    GPIO.output(OPEN_PIN, GPIO.LOW)
    GPIO.output(SOUND_PIN, GPIO.HIGH)
    GPIO.output(CLOSE_PIN, GPIO.HIGH)

def stop():
    clear()
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(OPEN_PIN, GPIO.OUT)
    GPIO.setup(CLOSE_PIN, GPIO.OUT)
    GPIO.setup(SOUND_PIN, GPIO.OUT)
    

    GPIO.output(OPEN_PIN, GPIO.LOW)
    GPIO.output(CLOSE_PIN, GPIO.LOW)

def clear():
    GPIO.cleanup()

clear()