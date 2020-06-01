import serial
import threading
import numpy as np
from queue import Queue 
from time import sleep, time

class InstructionsProcessor(object):
    def __init__(self, pqueue, seconds):
        super(InstructionsProcessor, self).__init__()
        self.pqueue = pqueue
        self.__byteQueue = Queue(0)
        self.__serialConnect = self.__setSerialConnection()
        self.__seconds = seconds
        self.endTime = time() + seconds
    
    def __setSerialConnection(self):
        temp = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=100000,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            timeout = None
        )
        return temp
    
    def run(self):
        byteRead(self.__byteQueue, self.__seconds)
        byteWrite(self.__byteQueue, self.__seconds, self.pqueue)
    
    def getSerialConnection(self):
        return self.__serialConnect

class byteRead(InstructionsProcessor, threading.Thread):
    def __init__(self, queue, seconds, priorityqueue = None):
        super(byteRead, self).__init__(priorityqueue, seconds)
        self.__queue = queue
        self.start()

    def run(self):
        data = [0]*25
        index = 0
        error_count= 0
        success_count =0

        print("Start...")

        while time() < self.endTime:
            inBytes = self.getSerialConnection().read()
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

class byteWrite(InstructionsProcessor, threading.Thread):
    def __init__(self, queue, seconds, priorityqueue):
        super(byteWrite, self).__init__(priorityqueue, seconds)
        self.__queue = queue
        self.start()

    def run(self):
        outBytes = [0]*25
        #channels = [0]*2
        channels = np.zeros((2,1))
        
        while time() < self.endTime:
            if not self.__queue.empty():
                outBytes = self.__queue.get()
                channels[0] = ((int.from_bytes(outBytes[1], byteorder='big') | int.from_bytes(outBytes[2], byteorder='big') << 8) & 2047)
                channels[1] = ((int.from_bytes(outBytes[2], byteorder='big') >> 3 | int.from_bytes(outBytes[3], byteorder='big') << 5) & 2047)
                self.pqueue.put((1, channels))
                
                #print("Data: ", outBytes)
                print("Channel 1: ", ((int.from_bytes(outBytes[1], byteorder='big') | int.from_bytes(outBytes[2], byteorder='big') << 8) & 2047))
                print("Channel 2: ", ((int.from_bytes(outBytes[2], byteorder='big') >> 3 | int.from_bytes(outBytes[3], byteorder='big') << 5) & 2047))