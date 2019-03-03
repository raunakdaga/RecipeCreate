import collections
import string
import re

# load text
filename = 'ingredients.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()
words = [word.lower() for word in words]

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]

print(words[:100])
