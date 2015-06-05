__author__ = 'JithinFin'

import _winreg as reg
from itertools import count

def getComPort():
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, 'HARDWARE\\DEVICEMAP\\SERIALCOMM')
    try:
        for i in count():
            device, port = reg.EnumValue(key, i)[:2]
            print device, port
            if (device.find("thcdcacm0") != -1):
                return ""+port
    except WindowsError:
        pass