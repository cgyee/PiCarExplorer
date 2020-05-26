import picamera
import picamera.array
import numpy as np
from time import sleep
import h5py

seconds = 1
out = h5py.File('data/images.h5', 'w')

with picamera.PiCamera() as camera:
    camera.resolution = (800, 600)
    camera.framerate = 30
    camera.start_recording('data/foo.h264')
    sleep(2)
    camera.wait_recording(seconds)
    images = np.zeros([30*seconds, 32, 32, 3])
    with picamera.array.PiRGBArray(camera, size = (32,32)) as stream:
        for i, fileName in enumerate(camera.capture_continuous(stream, resize=(32,32), format='rgb',
        use_video_port=True)):
            if i == 30*seconds:
                break
            images[i] = np.copy(stream.array)
            stream.truncate(0)
    camera.stop_recording()
    out.create_dataset("images", data=images, maxshape=(None, 32, 32, 3))
    #out.create_dataset("labels", data=rc_instruction, maxshape=(None,))
    out.close()