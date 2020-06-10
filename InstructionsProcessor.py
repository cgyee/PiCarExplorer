import serial
import threading
import numpy as np 
from queue import Queue 
from time import sleep

class Receiver(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.__pqueue = pqueue
        self.__run = True
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
        self.serial = cerial        
    
    def run(self):
        byteHelper = ByteHelper()
        while self.__run:
            if not self.__pqueue.full():
                self.__pqueue.put(
                (2, 
                byteHelper.setByte
                (byteHelper.getByte
                (self.serial))))
    
    def stop(self):
        self.__run= False
    
class ByteHelper():
    self.__data= np.zeros((2))
    self.__index= 0 
    self.__error_count= 0
    self.__success_count= 0

    def getByte(self, cnx):
        print("Starting Reading...")
        while self.__index<25:
            inBytes = cnx.read()
            if(inBytes!=b'\x0f' and index==0):
                pass
            else:
                self.__data[self.__index] = inBytes
                self.__index+=1
            if(self.__index==25):
                if(self.__data[24]) != b'\x00':
                    self.__error_count+=1
                else:
                    self.__success_count+=1
        print(self.__data)
        self.__index= 0
        return self.__data

    def setByte(self, inBytes):
        print("Starting Writing...")
        channel = np.zeros(2)
        if inBytes != None:
            channel[0] = (int.from_bytes(inBytes[1], byteorder='big') | int.from_bytes(inBytes[2], byteorder='big') << 8) & 2047
            channel[1] = (int.from_bytes(inBytes[2], byteorder='big') >> 3 | int.from_bytes(inBytes[3], byteorder='big') << 5) & 2047
        return channel