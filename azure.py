########### Python 3.6 #############
import requests, base64
import speak

headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
}

params = {
    # Request parameters. All of them are optional.
    'visualFeatures': 'Description',
    'language': 'en',
}

# Replace the three dots below with the full file path to a JPEG image of a celebrity on your computer or network.
image = open('now.jpg','rb').read() # Read image file in binary mode

try:
    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
    #   URL below with "westus".
    response = requests.post(url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze',
                             headers = headers,
                             params = params,
                             data = image)
    data = response.json()
    res = data['description']['captions'][0]['text']
    speak.speak(res)
    #print(data)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################
