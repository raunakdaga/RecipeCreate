import re
import string
#x = "This is a sentence. (once a day) [twice a day]"
#re.sub("[\(\[].*?[\)\]]", "", x)

toRemove = "''!()-[]{};-:',<>./?@#$%^&*_1234567890'"
noPunct = "";

with open("ingredients.txt", "r+") as f:
    for line in f:
        for char in line:
            if char not in toRemove:
                noPunct = noPunct+char
noPunct.lower()

print(noPunct)
