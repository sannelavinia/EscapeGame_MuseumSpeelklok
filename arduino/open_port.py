import serial
import os
import time
import serial.tools.list_ports

def port_name:
   
    try:

        ports = list(serial.tools.list_ports.comports())
        for p in ports:

    # arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)  

            serialcomm = serial.Serial(p.name, 9600)

            serialcomm.timeout = 1

            return serialcomm

                # i = input("Enter Input: ").strip()

                # i = active
                
                # serialcomm.write(i.encode())

                # time.sleep(0.1)

                # s = 'stop'

                # if s in serialcomm.readline().decode():
                    # break

            # serialcomm.close()

    except:
        return "$"
