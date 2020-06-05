import ImageProcessor
import cmdInterface
import InstructionsProcessor
from queue import PriorityQueue
from multiprocessing import Queue
from time import time, sleep

#x = cmdInterface.cmdInterface()
if __name__ == "__main__":
    #args = x.getArgs()
    #seconds = int(args.s)
    
    #q = PriorityQueue()
    q = Queue()
    image = ImageProcessor.Camera(q)
    instruct = InstructionsProcessor.Receiver(q)
    instruct.setup()
    image.setup()

    startTime = time()
    endTime = time()
    
    image.start()
    instruct.start()
    while time() < endTime + 3:
        instruct.run()
        image.run()

    