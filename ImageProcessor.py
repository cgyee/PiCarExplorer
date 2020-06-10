import picamera
import numpy as np
import h5py
import threading
from time import sleep

class Camera(threading.Thread):
    def __init__(self, pqueue):
        super().__init__()
        self.__pqueue= pqueue
        self.__run= True
        self.__images = np.zeros((1, 32 ,32, 3))
        self.__labels = np.zeros((1,2))

    def setup(self):
        pass

    def run(self):
        self.__getImages()
             
    def stop(self):
        self.__run= False

    def __getImages(self):
        while self.__run:
            if not self.__pqueue.empty():
                with picamera.PiCamera() as camera:
                    with picamera.array.PiRGBArray(camera, size = (32,32)) as stream:
                        print("Starting Capturing...")
                        camera.capture(stream, resize=(32,32), format='rgb', use_video_port=True)
                        self.__images = np.copy(stream.array)
                        temp = list(self.__pqueue.get())
                        self.__labels[0][0] = temp[1][0]
                        self.__labels[0][1] = temp[1][1]                    
                fileWriter().writeToFile(self.__images, self.__labels)

class fileWriter():
    def writeToFile(self, images, labels):
        with h5py.File('data/images.h5', 'a') as hf:
            hf['images'].resize((hf['images'].shape[0]+images.shape[0]), axis=0)
            hf['labels'].resize((hf['labels'].shape[0]+labels.shape[0]), axis=0)
            hf['images'][hf['images'].shape[0]-1] = images
            hf['labels'][hf['labels'].shape[0]-1] = labels