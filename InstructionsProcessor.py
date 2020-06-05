import serial
import threading
import _thread 
from queue import Queue 
from time import sleep

class InstructionsProcessor(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.__queue = pqueue
        self.serial = None
    
    def setup(self):
        cerial = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=100000,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            timeout = None
        )
        self.serial 
        
    
    def run(self):
        byteRead(self.__queue, self.__byteQueue)
        byteWrite(self.__queue, self.__byteQueue)
    
    def getConnection(self):
        return self.__serialConnect

class byteRead(InstructionsProcessor):
    def __init__(self,pq, queue):
        super(byteRead, self).__init__(pq)
        self.__queue = queue
        self.start()

    def run(self):
        data = [0]*25
        index = 0
        error_count= 0
        success_count =0
        print("Start...")
        while True:
            inBytes = self.getConnection().read()
            if(inBytes!=b'\x0f' and index==0):
                pass
            else:
                data[index] = inBytes
                index+=1
            if(index == 25):
                if(data[24]) != b'\x00':
                    error_count+=1
                else:
                    success_count+=1
                index=0
                temp = data[:]
                self.__queue.put(temp)

class byteWrite(InstructionsProcessor):
    def __init__(self, pq, queue):
        super(byteWrite, self).__init__(pq)
        self.__queue = queue
        self.start()

    def run(self):
        outBytes = [0]*25
        channels = [0]*2
        while True:
            if not self.__queue.empty():
                outBytes = self.__queue.get()
                print("Data: ", outBytes)
                print("Channel 1: ", ((int.from_bytes(outBytes[1], byteorder='big') | int.from_bytes(outBytes[2], byteorder='big') << 8) & 2047))
                print("Channel 2: ", ((int.from_bytes(outBytes[2], byteorder='big') >> 3 | int.from_bytes(outBytes[3], byteorder='big') << 5) & 2047))