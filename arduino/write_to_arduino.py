import serial
import os
import time
import serial.tools.list_ports
def send_message(serial_message, active):

    try:
            i = active
            serial_message.write(i.encode())
            time.sleep(0.1)


    except:
        return
