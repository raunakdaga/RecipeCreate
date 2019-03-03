import io
import os
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
file_name = os.path.join(os.path.dirname(__file__), 'apple.jpg')

foods = []

def getLabels(albumid):
    for fileID in os.listdir(albumid):
        file_name = os.path.join(os.path.dirname(__file__), (albumid + '/' + fileID))
        with io.open(file_name, 'rb') as image:
            content = image.read()

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            if(label in open('ingredients.txt', 'r').read().split('/n')):
                foods.append(label.description)
