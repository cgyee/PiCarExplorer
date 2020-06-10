import serial
import threading
import _thread 
from queue import Queue 
from time import sleep

class Receiver(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.__pqueue = pqueue
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
            byteHelper = byteOrder()
            self.__pqueue.put(
            (2, 
            byteHelper.setByte
            (byteHelper.getByte
            (self.serial))))
    
class byteOrder():
    def getByte(self, cnx):
        data = [0]*25
        index = 0
        error_count = 0
        success_count = 0
        print("Starting Reading...")
        while index<25:
            inBytes = cnx.read()
            if(inBytes!=b'\x0f' and index==0):
                pass
            else:
                data[index] = inBytes
                index+=1
            if(index==25):
                if(data[24]) != b'\x00':
                    error_count+=1
                else:
                    success_count+=1
        print(data)
        return data

    def setByte(self, inBytes):
        print("Starting Writing...")
        channel = [0]*2
        if inBytes != None:
            channel[0] = (int.from_bytes(inBytes[1], byteorder='big') | int.from_bytes(inBytes[2], byteorder='big') << 8) & 2047
            channel[1] = (int.from_bytes(inBytes[2], byteorder='big') >> 3 | int.from_bytes(inBytes[3], byteorder='big') << 5) & 2047
            #print(channel)
        return channel