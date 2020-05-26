import picamera
import picamera.array
import numpy as np
import h5py
import threading
from time import sleep
from queue import PriorityQueue

class ImageProcessor(threading.Thread):
    def __init__(self, pqueue, seconds):
        super(ImageProcessor, self).__init__()
        self.start()
        self.__seconds = seconds
        self.__queue = pqueue

    def run(self):
        imageData = h5py.File('data/images.h5', 'w')

        with picamera.PiCamera() as camera:
            camera.resolution = (800, 600)
            camera.framerate = 30
            camera.start_recording('data/foo.h264')
            sleep(2)
            camera.wait_recording(self.__seconds)

            images = np.zeros([30*self.__seconds, 32, 32, 3])
            labels = np.zeros([30*self.__seconds, ])
            with picamera.array.PiRGBArray(camera, size = (32,32)) as stream:
                for i, fileName in enumerate(camera.capture_continuous(stream, resize=(32,32), 
                    format='rgb', use_video_port=True)):

                    if i == 30*self.__seconds:
                        break
                    
                    images[i] = np.copy(stream.array)
                    #labels[i] = self.__queue.get(True)
                    stream.truncate(0)

            camera.stop_recording()
            imageData.create_dataset("images", data=images, maxshape=(None, 32, 32, 3))
            #imageData.create_dataset("labels", data=rc_instruction, maxshape=(None,))
            imageData.close()