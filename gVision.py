import picamera, io
from google.cloud import vision
from google.cloud.vision import types
import speak

def detect_labels(path, doLabel=True, doLogo=False, doText=False, doSafe=False):
	"""Detects labels in the file."""
	labelList = []
	asdf = []
	client = vision.ImageAnnotatorClient()
	possibleDanger = ['POSSIBLE','LIKELY','VERY LIKELY']

	with io.open(path, 'rb') as image_file:
		content = image_file.read()
 
	image = types.Image(content=content)

# LABELS
	if doLabel:
		response = client.label_detection(image=image)
		print response
		labels = response.label_annotations
		print('Labels:')
		i = 0	
		for label in labels:
			print(label.description)
			if i <= 2:
				labelList.append(labels[i].description)
			i+=1
# LOGOS
	if doLogo:
		response = client.logo_detection(image=image)
		logos = response.logo_annotations
		print('Logos:')

		for logo in logos:
			print(logo.description)
		if len(logos):
			asdf.append('i see logo: '+logos[0].description)

# TEXTS
	if doText:
		response = client.text_detection(image=image)
		texts = response.text_annotations
		print('Texts:')

		for text in texts:
			print('\n"{}"'.format(text.description))
		if len(texts):
			asdf.append('I read: '+texts[0].description)
# SAFE SEARCH
	if doSafe:    
		response = client.safe_search_detection(image=image)
		safe = response.safe_search_annotation

		# Names of likelihood from google.cloud.vision.enums
		likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
						   'LIKELY', 'VERY_LIKELY')
		print('Safe search:')

		print('adult: {}'.format(likelihood_name[safe.adult]))
		print('medical: {}'.format(likelihood_name[safe.medical]))
		print('spoofed: {}'.format(likelihood_name[safe.spoof]))
		print('violence: {}'.format(likelihood_name[safe.violence]))
		
		if safe.adult in possibleDanger:
			asdf.append('adult ' + safe.adult)
		if safe.medical in possibleDanger:
			asdf.append('medical ' + safe.medical)
		if safe.spoof in possibleDanger:
			asdf.append('spoofed ' + safe.spoof)
		if safe.violence in possibleDanger:
			asdf.append('violence ' + safe.violence)
	return labelList, asdf
def main(filename):
	labelList, res = detect_labels('/home/raspi/Desktop/'+filename,True,True,True,True)
	print labelList, res

	speak.speak(speak.stringify(labelList, True) +' '+ speak.stringify(res))
	#speak.speak('helo')
if __name__ == '__main__':
	main()
