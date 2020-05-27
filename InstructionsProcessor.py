import serial

class InstructionsProcessor(threading.Thread):
    def __init__(self, pqueue):
        super(InstructionsProcessor, self).__init__()
        self.__queue = pqueue
        self.__serialConnect = None
        self.__serialConnection(self.__serialConnect)
        self.start()
    
    def __serialConnection(coonnection):
        serial = serial.Serial(
            port = '/dev/serial0',
            baudrate = 100000,
            parity = serial.PARITY_EVEN
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            timeout= None
        )
        connection= serial

    def run(self):
        data = [25]
        index = 0
        while True:
           rc_byte = self.
           if(byte != 0x0F or byte != 0x00):
               data[index] = byte
               index +=1
            else:
                data[index] = byte