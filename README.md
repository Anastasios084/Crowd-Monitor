# Crowd-Monitor

This is a script written in micro python for the Raspberry pi pico W.

## Components used:
- 1 x Raspberry Pi Pico W
- 2 x ultrasound sensors HC-SR04
- 2 x LEDs (in this case red and green)
- 2 x 100 Ohms Resistors
- 1 x Breadboard
- 40 x pin headers
- 10 x DuPont cables

## What does it do?

Well this script uses these two ultrasound sensors to determine if a person has exited or entered a room

## What needs to be implemented?

Thus far determining if a person has entered or exited a room has implemented, the main concept that I have is that I want this script to adjust to its surroundings.

The one thing that follows this logic is the triggering distance, by sampling 100 times the distance of the sensors. This should be followed for achieving high accuracy

So what's left? These:
- Making the script/device autonomous from my pc
- Counting the people in the room
- Sending this information over the internet (IMPORTANT)
- Sending logs to a central server
- Recovery from errors (ALSO IMPORTANT)
- Protect the device if stolen with a password

The last one is VERY important, because if a device is stolen, all the data and the servers, the credentials that this device uses will be exposed and this is a HUGE security hazard. 
