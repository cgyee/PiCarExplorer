import ImageProcessor
import cmdInterface
import InstructionsProcessor
import ESC_Controller
from queue import PriorityQueue
from multiprocessing import Queue
from time import time, sleep

#x = cmdInterface.cmdInterface()
if __name__ == "__main__":
    #args = x.getArgs()
    #seconds = int(args.s)
    
    #q = PriorityQueue()
    q = Queue()

    #image = ImageProcessor.Camera(q)
    instruct = InstructionsProcessor.Receiver(q)
    throttle = ESC_Controller.ServoDriver(q)

    #image.setup()
    instruct.setup()
    throttle.setup()

    startTime = time()
    endTime = time()
    
    #image.start()
    instruct.start()
    throttle.start()
    throttle.stopMotor()

    while time() < endTime + 3:
        #image.run()
        instruct.run()
        throttle.run()
    instruct.join()
    throttle.stopMotor()
    throttle.join()


    