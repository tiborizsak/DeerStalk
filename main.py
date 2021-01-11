import statistics
import serial
import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (1920, 1080)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()