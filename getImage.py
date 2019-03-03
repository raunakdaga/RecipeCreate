import io
import os
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
file_name = os.path.join(os.path.dirname(__file__), 'apple.jpg')

with io.open(file_name, 'rb') as image:
    content = image.read()

image = types.Image(content=content)

response = client.label_detection(image=image)

labels = response.label_annotations

print('Labels: ')

foods = []
for label in labels:
    # nikos method to check for if something is within the list.txt
    foods.append(label.description)
