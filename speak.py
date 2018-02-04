import serial, time

serial = serial.Serial('/dev/serial0', baudrate=9600)
def speak(stringy):
	print 'speaking: '+stringy
	
	serial.close()
	serial.open()
	serial.write('\n')
	serial.write('V18\n') #volume
	data = ''
	i = 0
	while (data!=':'):
		data = serial.read()
		print 'reading serial '+str(i)
		i=i+1
	serial.write('S%s' % (stringy.encode()))
	#serial.write(stringy.encode())
	serial.write('\n')
	serial.close()

def stringify(array, labels=False):
	if labels:
		a = 'Your view can be described by '
	else:
		a = ''
	for x in array:
		a = a + x + ' '
	print a
	return a		
