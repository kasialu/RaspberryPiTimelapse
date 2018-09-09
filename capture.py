
from datetime import datetime
import logging
import os
from time import sleep

from picamera import PiCamera
import toml
import dropbox

with open('/home/pi/timelapse/config.toml', 'r') as fo:
    config = toml.load(fo)

LOG_PATH = '/home/pi/timelapse/log/camera.log'
logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG)

IMAGE_PATH = '/home/pi/timelapse/images'
DBOX_DESTINATION = '/Apps/Raspberry Pie Camera'


def send_to_dropbox(fpath, destination):
	'''
	Send a file to Dropbox
	'''

	with open(fpath, 'rb') as fo:
		data = fo.read()

	fname = os.path.basename(fpath)

	try:
		res = dbx.files_upload(data, '{}/{}'.format(destination, fname))
	except Exception as e:
		logging.error('Exception occured: {}'.format(str(e)))


if __name__ == '__main__':
	
	dbx = dropbox.Dropbox(config['dropbox']['ACCESS_TOKEN'])
	
	with  PiCamera() as camera:
		
		camera.resolution = (1280, 720)
		camera.brightness = 50
		camera.zoom = (0.0, 0.0, 1.0, 1.0)

		while True:
			dt = datetime.now().isoformat()
			fpath = os.path.join(IMAGE_PATH, 'img_{}.jpg'.format(dt))
			camera.annotate_text = dt
			camera.capture(output=fpath)
			logging.info('saving {}'.format(fpath))
			logging.info('sending to dropbox ...')
			send_to_dropbox(fpath, DBOX_DESTINATION)
			logging.info('sending to dropbox done.')
			sleep(30)

