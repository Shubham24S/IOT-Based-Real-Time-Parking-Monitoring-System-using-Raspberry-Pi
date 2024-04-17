# pip install requests

serverUrl = "https://6ddfa90e-049f-4374-ab44-333bf5be0e75-00-1wnbb1w45319c.kirk.replit.dev"

#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import requests


print("Car Parking System : Setup Started")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

'''
Define pin for sensors
'''
slot1_Sensor = 29
slot2_Sensor = 31
slot3_Sensor = 33
GPIO.setup(slot1_Sensor, GPIO.IN)
GPIO.setup(slot2_Sensor, GPIO.IN)
GPIO.setup(slot3_Sensor, GPIO.IN)

print("Car Parking System : Setup Complete")

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
# set_servo_angle(90)


def update_slot_status(slot, status):
    url = f'{serverUrl}/update?slot={slot}&status={status}'
    response = requests.get(url)

    if response.status_code == 200:
        print(f'Success: Slot {slot} status updated to {status}')
    elif response.status_code == 404:
        print(f'Error: Slot {slot} does not exist')
    else:
        print(f'Error: Something went wrong. Status code {response.status_code}')

# Example usage
# update_slot_status('slot2', 'on')



# Define delay between readings
delay = 5

print("Car Parking System : System Begins")
while 1:
    slot1_status = GPIO.input(slot1_Sensor)
    time.sleep(1.8)
    slot2_status = GPIO.input(slot2_Sensor)
    slot3_status = GPIO.input(slot3_Sensor)
    time.sleep(1.8)

    if slot1_status == False:
        # Do something when Slot 1 is occupied
        print("Slot 1 is occupied")
        update_slot_status('slot1', 'off')

        time.sleep(2.8)
    else:
        # Do something when Slot 1 is free
        print("Slot 1 is free")
        update_slot_status('slot1', 'on')

        time.sleep(2.8)



    if slot2_status == False:
        # Do something when Slot 2 is occupied
        print("Slot 2 is occupied")
        update_slot_status('slot2', 'off')

        time.sleep(2.8)
    else:
        # Do something when Slot 2 is free
        print("Slot 2 is free")
        update_slot_status('slot2', 'on')

        time.sleep(2.8)

    if slot3_status == False:
        # Do something when Slot 1 is occupied
        print("Gate : Servo Up")
        # set_servo_angle(90)
        set_servo_angle(0)

        # update_slot_status('slot1', 'off')

        time.sleep(2.8)
    else:
        # Do something when Slot 1 is free
        print("Gate : Servo Down")
        set_servo_angle(180)

        # update_slot_status('slot1', 'on')

        time.sleep(2.8)


print("Car Parking System : System Ends")


'''
Pin connections of Ir Module & rpi


# ir sensor 1 :
- out = pin 29
- Vcc = pin 2 (5v Power)
- Gnd = pin 6 (GND)

# ir sensor 2 :
- out = pin 31
- Vcc = pin 4 (5v Power)
- Gnd = pin 9 (GND)


https://6a79193f-6605-44e3-90fd-90cf4c111036-00-1hcnyifnrpkd8.riker.replit.dev/update?slot=slot2&status=on

'''
