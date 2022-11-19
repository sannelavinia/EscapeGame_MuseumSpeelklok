import serial

import time
import serial.tools.list_ports


ports = list(serial.tools.list_ports.comports())
for p in ports:

    # arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)  


    serialcomm = serial.Serial(p.device, 9600)

    serialcomm.timeout = 1

    while True:

        i = input("Enter Input: ").strip()

        if i == "Done":

            print('finished')

            break

        serialcomm.write(i.encode())

        time.sleep(0.5)

        print(serialcomm.readline().decode('ascii'))

    serialcomm.close()