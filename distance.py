from gpiozero import DistanceSensor
from time import sleep, time
import threading

class DistanceTracking(threading.Thread):
    def __init__(self, pqueue, seconds):
        super(DistanceTracking, self).__init__()
        self.__queue = pqueue
        self.__seconds =seconds
        self.start()

    def run(self):
        distanceSensor = DistanceSensor(echo=24, trigger=23)
        endTime = time() + self.__seconds
        while time() < endTime:
            #if(distanceSenor.distance <=10):
            #    pqueue.put((1, "stop"))
            #    sleep(5)
            print("Distance: ", distanceSensor.distance)
            sleep(1)