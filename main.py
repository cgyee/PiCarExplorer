import ImageProcessor
import cmdInterface
import InstructionsProcessor
from queue import PriorityQueue
from time import time, sleep

#x = cmdInterface.cmdInterface()

if __name__ == "__main__":
    #args = x.getArgs()
    #seconds = int(args.s)
    pqueue = PriorityQueue()
    endTime = time()
    image = ImageProcessor.ImageProcessor(pqueue)
    instruct = InstructionsProcessor.InstructionsProcessor(pqueue)
    sleep(2)
    
    instruct.setup()
    image.setup()
    instruct.start()
    image.start()

    while time() < endTime + 3:
        instruct.run()
        image.run()
    print("Done!!!!")


    