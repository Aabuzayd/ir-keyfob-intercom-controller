import time
import logging

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


class IntercomController:
    def __init__(self, relay_pin: int = 27, unlock_seconds: float = 3.0):
        self.relay_pin = relay_pin
        self.unlock_seconds = unlock_seconds

        if GPIO is not None:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.relay_pin, GPIO.OUT, initial=GPIO.LOW)
        else:
            logging.warning("RPi.GPIO is not available. Running in simulation mode.")

    def unlock(self):
        if GPIO is None:
            logging.info("Simulation mode: relay would be energized for %.1f sec", self.unlock_seconds)
            time.sleep(self.unlock_seconds)
            return

        logging.info("Unlocking intercom relay for %.1f sec", self.unlock_seconds)
        GPIO.output(self.relay_pin, GPIO.HIGH)
        time.sleep(self.unlock_seconds)
        GPIO.output(self.relay_pin, GPIO.LOW)

    def cleanup(self):
        if GPIO is not None:
            GPIO.cleanup(self.relay_pin)
