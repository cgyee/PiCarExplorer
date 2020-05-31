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

    #called when self.start() is called
    def run(self):
        #open h5 as a writeable file
        imageData = h5py.File('data/images.h5', 'w')

        #Check if the picamera is available and if it is execute the following code block
        with picamera.PiCamera() as camera:
            #Setting up the camerea
            camera.resolution = (1920, 1080)
            camera.framerate = 30
            camera.start_recording('data/foo.h264')
            sleep(2)
            camera.wait_recording(self.__seconds)

            #Defining np arrays for data storage of images and corresponding receiver instructions(labels)
            images = np.zeros([30*self.__seconds, 32, 32, 3])
            labels = np.zeros([30*self.__seconds, ])

            #Check if picamera is available and if it is execute the following code block
            with picamera.array.PiRGBArray(camera, size = (32,32)) as stream:
                for i, fileName in enumerate(camera.capture_continuous(stream, resize=(32,32), 
                    format='rgb', use_video_port=True)):

                    #Break out of loop after caputuring 30 images * time to get around 30FPS of images
                    if i == 30*self.__seconds:
                        break
                    
                    images[i] = np.copy(stream.array)
                    #labels[i] = self.__queue.get(True)
                    stream.truncate(0)

            camera.stop_recording()

            #Write the results to h5 file for later use
            imageData.create_dataset("images", data=images, maxshape=(None, 32, 32, 3))
            #imageData.create_dataset("labels", data=rc_instruction, maxshape=(None,))
            imageData.close()