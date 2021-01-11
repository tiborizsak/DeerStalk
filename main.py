import statistics
import serial
import picamera
from fractions import Fraction
from time import sleep

with picamera.PiCamera() as camera:
    #This section is used in case of low light capture
    # camera.framerate = Fraction(1, 6)
    # camera.sensor_mode = 3
    # camera.shutter_speed = 6000000
    # camera.iso = 300
    # sleep(30)
    # camera.exposure_mode = 'off'
    camera.rotation = 180
    camera.resolution = (1920, 1080)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()