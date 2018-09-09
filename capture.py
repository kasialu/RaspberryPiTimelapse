
from datetime import datetime
import logging
import os
from time import sleep
from picamera import PiCamera

LOG_PATH = '/home/pi/timelapse/log/camera.log'
logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG)

IMAGE_PATH = '/home/pi/timelapse/images'


if __name__ == '__main__':
	
	with  PiCamera() as camera:
		
		camera.resolution = (1280, 720)
		camera.brightness = 50
		while True:
			dt = datetime.now().isoformat()
			fname = os.path.join(IMAGE_PATH, 'img_{}.jpg'.format(dt))
			camera.annotate_text = dt
			camera.capture(output=fname)
			logging.info('saving {}'.format(fname))
			sleep(30)

