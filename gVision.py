import picamera, io
from google.cloud import vision
from google.cloud.vision import types

def detect_labels(path, doLabel=True, doLogo=False, doText=False, doSafe=True):
	"""Detects labels in the file."""
	client = vision.ImageAnnotatorClient()

	with io.open(path, 'rb') as image_file:
		content = image_file.read()
 
	image = types.Image(content=content)

# LABELS
	if doLabel:
		response = client.label_detection(image=image)
		print response
		labels = response.label_annotations
		print('Labels:')

		for label in labels:
			print(label.description)
# LOGOS
	if doLogo:
		response = client.logo_detection(image=image)
		logos = response.logo_annotations
		print('Logos:')

		for logo in logos:
			print(logo.description)

# TEXTS
	if doText:
		response = client.text_detection(image=image)
		texts = response.text_annotations
		print('Texts:')

		for text in texts:
			print('\n"{}"'.format(text.description))

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

def main(filename):
	detect_labels('/home/raspi/Desktop/'+filename)
if __name__ == '__main__':
	main()
