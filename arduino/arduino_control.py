# deze functie is om een code (active) naar arduino sturen

import serial

import time
import serial.tools.list_ports

def arduino(active):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        
        # arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)  


        serialcomm = serial.Serial(p.device, 9600)

        serialcomm.timeout = 0.1
        x=0
        while x<10:

            # i = input("Enter Input: ").strip()
            i = str(active)

            # if i == "Done":

            #     print('finished')

            #     break

            serialcomm.write(i.encode())

            # time.sleep(0.1)
            x+=1
            print(serialcomm.readline().decode('ascii'))
            
        serialcomm.close()