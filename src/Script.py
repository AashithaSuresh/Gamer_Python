from Serial import getComPort

__author__ = 'Jithin M Das'

from Keystroke import SendInput, Keyboard, KEYEVENTF_EXTENDEDKEY, VK_LEFT, VK_RIGHT, KEYEVENTF_KEYUP
import time, sys
import serial
import time

portConnected = getComPort()
print portConnected
ser = serial.Serial(port = str(portConnected), baudrate=38400, timeout=0)

while 1:
    try:
        keypress = ser.read()
        #print(keypress)
        if (keypress == 'l'):
            SendInput(Keyboard(VK_LEFT))
            time.sleep(0.2)
            print('Left')
        elif (keypress == 'r'):
            SendInput(Keyboard(VK_RIGHT))
            time.sleep(0.2)
            print('Right')

    except ser.SerialTimeoutException:
        print('Data could not be read')
