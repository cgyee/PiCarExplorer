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
    
    q = PriorityQueue()
    #q = Queue()
    car = []

    image = ImageProcessor.Camera(q)
    instruct = InstructionsProcessor.Receiver(q)
    throttle = ESC_Controller.ServoDriver(q)
    car.append(instruct)
    car.append(throttle)
    #car.append(image)

    startTime = time()
    endTime = time()
    
    #image.start()
    #instruct.start()
    #throttle.start()

    for components in car:
        components.setup()
        components.start() 
    while time() < endTime + 3:
        pass
    for components in car:
        components.stop()
        components.join()


    