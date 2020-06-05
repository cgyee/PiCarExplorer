from gpiozero import DistanceSensor
from time import sleep, time
import threading

class DistanceTracking(threading.Thread):
    def __init__(self, pqueue, seconds):
        super().__init__()
        self.__pqueue = pqueue
        self.__distanceSensor

    def setup(self):
        self.distanceSensor = DistanceSensor(echo=24, trigger=23)

    def run(self):
        if(self.sensor.distanceSensor <= 10):
            self.__pqueue.put((1,(1,1)))