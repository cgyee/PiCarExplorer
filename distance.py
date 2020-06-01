from gpiozero import DistanceSensor
from time import sleep, time
import numpy as np
import threading

class DistanceTracking(threading.Thread):
    def __init__(self, pqueue, seconds):
        super(DistanceTracking, self).__init__()
        self.__queue = pqueue
        self.__seconds =seconds

    def run(self):
        distanceSensor = DistanceSensor(echo=24, trigger=23)
        endTime = time() + self.__seconds
        while time() < endTime:
            print("Distance: ", distanceSensor.distance)
            #if(distanceSenor.distance <=10):
            #    pqueue.put((1, np.zeros((2,1))))
            #    sleep(3)
            sleep(2)