import RPi.GPIO as GPIO
import gVision
import time
import picamera

def main():
	print 'Starting...'
	camera = picamera.PiCamera()
	filename='now.jpg'
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
	i = 0
	try:
		while True:
			i=i+1
#			print('Sleeping...'+str(i))
#			time.sleep(2)
			button_state = GPIO.input(23)
			if not button_state:
				print 'button pressed!'
				camera.capture(filename)
				gVision.main(filename)
	except Exception as e: 
		print e
		GPIO.cleanup()

if __name__ == '__main__':
	main()
