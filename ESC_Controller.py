import multiprocessing
import threading
import adafruit_servokit
import adafruit_motor
from time import sleep

class ServoDriver(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.kit = adafruit_servokit.ServoKit(channels=16)
        self.pqueue = pqueue
        self.__last_speed=0
        self.__run = True

    def setup(self):
        pass

    def run(self):
        self.setThrottleSteering()

    def setThrottleSteering(self):
        while self.__run:
            if not self.pqueue.empty():
                data = self.pqueue.get()
                if data[1][0] > 1024:
                    self.__last_speed= .1
                else:
                    self.__last_speed= -.1
                print("Throttle and Steering", (data[1][0]//1024)*.5, self.__last_speed)
                self.kit.continuous_servo[0].throttle= self.__last_speed
            else:
                self.kit.continuous_servo[0].throttle= self.__last_speed

    def stop(self):
        self.__run= False
        self.stopMotor()
    
    def stopMotor(self):
        self.kit.continuous_servo[0].throttle=0
        sleep(1)
        print("Stop motor done")
