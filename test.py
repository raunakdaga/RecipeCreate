import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(open('ingredients.txt', 'r').read().split('\n'))
