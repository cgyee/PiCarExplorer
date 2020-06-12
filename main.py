import ImageProcessor
import cmdInterface
import InstructionsProcessor
import ESC_Controller
from queue import PriorityQueue
from time import time, sleep

#x = cmdInterface.cmdInterface()
if __name__ == "__main__":
    #args = x.getArgs()
    #seconds = int(args.s)
    
    q = PriorityQueue(maxsize=1)
    car = []

    car.append(InstructionsProcessor.Receiver(q))
    car.append(ESC_Controller.MotorDriver(q))
    #car.append(ImageProcessor.Camera(q))

    startTime = time()
    endTime = time()
    
    for components in car:
        components.setup()
    
    for components in car:
        components.start()

    while time() < endTime + 5:
        pass
    for components in car:
        components.stop()
        components.join()