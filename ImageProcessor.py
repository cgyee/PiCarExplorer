import picamera
import picamera.array
import numpy as np
import h5py
import threading
from time import sleep
from queue import PriorityQueue

class ImageProcessor(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.__pqueue = pqueue
        self.__videoCamera = None
        self.__captureCamera = None

    def setup(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (600, 600)
            camera.framerate = 30
            self.__videoCamera = camera
            with picamera.array.PiRGBArray(camera, size = (32,32)) as stream:
                self.__captureCamera = stream
    
    def writeToFile(self):
        with h5py.File('data/images.h5', 'a') as hf:
            hf.resize(hf.shape[0][0]+30, axis = 0)
        return h5py

    def run(self):
        if not self.__pqueue.empty():
            images = np.zeros((30, 32, 32, 3))
            labels = np.zeros((30, 2, 1))
            for i, fileName in enumerate(self.__videoCamera.capture_continous(self.__captureCamera, (32,32),
            format='rgb', use_video_port = True)):

                if(i == 30):
                    break
                
                images[i] = np.copy(self.__captureCamera)
                labels[i] = np.asarray(self.__pqueue.get())

            out = writeToFile()
            out['images'] = images
            out['labels'] = labels