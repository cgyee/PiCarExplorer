import ImageProcessor
import distance
import cmdInterface
import InstructionsProcessor
from queue import PriorityQueue
from time import time, sleep

#x = cmdInterface.cmdInterface()

if __name__ == "__main__":
    #args = x.getArgs()
    #seconds = int(args.s)
    pqueue = PriorityQueue(maxsize=3)
    #ImageProcessor.ImageProcessor(pqueue, seconds)
    #distance.DistanceTracking(pqueue, seconds)
    InstructionsProcessor.InstructionsProcessor(pqueue)