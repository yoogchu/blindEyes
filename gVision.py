import picamera, io
from google.cloud import vision
from google.cloud.vision import types

filename = 'now.jpg'
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        print type(content)
 
    image = types.Image(content=content)

    response = client.label_detection(image=image)
    print response
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

camera = picamera.PiCamera()
camera.capture(filename)
detect_labels('/home/raspi/Desktop/'+filename)

