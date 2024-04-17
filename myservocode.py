# Servo Code

# pip install gpiozero

from gpiozero import Servo
from time import sleep

def set_servo_angle(angle):
    # Set pin connected to the servo
    servo_pin = 17

    # Create a Servo object
    servo = Servo(servo_pin)

    try:
        # Convert angle to a value between -1 (0 degrees) and 1 (180 degrees)
        angle_value = (angle / 180.0) * 2 - 1

        # Set the servo to the specified angle
        servo.value = angle_value
        sleep(1)  # Adjust delay as needed for your servo to reach the position

    finally:
        servo.close()  # Clean up servo resources

# Example usage:
# Rotate servo to 90 degrees
set_servo_angle(90)
