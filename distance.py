from gpiozero import DistanceSensor
from time import sleep
import threading

class DistanceTracking(threading.Thread):
    def __init__(self, pqueue):
        super(DistanceTracking, self).__init__()
        self.__queue = pqueue
        self.start()

    def run(self):
        distanceSensor = DistanceSensor(echo=24, trigger=23)
        while True:
            #if(distanceSenor.distance <=10):
            #    pqueue.put((1, "stop"))
            #    sleep(5)
            print("Distance: ", distanceSensor.distance)