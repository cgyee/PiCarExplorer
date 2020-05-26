import ImageProcessor
import distance
from queue import PriorityQueue

if __name__ == "__main__":
    pqueue = PriorityQueue(maxsize=3)
    ImageProcessor.ImageProcessor(pqueue)
    distance.DistanceTracking(pqueue)