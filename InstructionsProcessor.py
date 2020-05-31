import serial
import threading
from time import sleep

class InstructionsProcessor(threading.Thread):
    def __init__(self, pqueue):
        super(InstructionsProcessor, self).__init__()
        self.__queue = pqueue
        self.__serialConnect = self.__serialConnection()
        self.start()
    
    def __serialConnection(self):
        temp = serial.Serial(
            port='/dev/serial0',
            #port='/dev/ttyUSB0',
            baudrate=100000,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
        )
        return temp

    def run(self):
        data = [0]*25
        index = 0
        error_count= 0
        success_count =0
        print("Start...")
        while True:
            rc_bytes = self.__serialConnect.read()
            if(rc_bytes!=b'\x0f' and index==0):
                pass
            else:
                data[index] = rc_bytes
                print(rc_bytes, index)
                index+=1
            if(index == 25):
                if(data[24]) != b'\x00':
                    error_count+=1
                else:
                    success_count+=1
                index=0
                channels = [0]*2
                channels[0] = ((int.from_bytes(data[1], byteorder='big') | int.from_bytes(data[2], byteorder='big') << 8) & 2047)
                channels[1] = ((int.from_bytes(data[2], byteorder='big') >> 3 | int.from_bytes(data[3], byteorder='big') << 5) & 2047)
                print("Errors: ", error_count)
                print("Success terminated: ", success_count)
                print("Ratio of success: ", success_count//(success_count+error_count))
                print("Channel 1: ", channels[0])
                print("Channel 2: ", channels[1])
                #print("stop")
                #sleep(3)