import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
from math import cos, sin

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setGrayColor(color):
    return [color, color, color]


img = Image.open('low.png')
img = numpy.asarray(img)

# copy list not reference
ht = deepcopy(img)

h = [0] * 255
count =  0

s = [0] * 255
sum = 0

nh = [0] * 255

for i in range(len(img)):
    for j in range(len(img[i])):
        count += 1
        h[getGrayColor(img[i][j])] += 1

for i in range(len(h)):
    sum += h[i]
    s[i] = int(sum/count*254)

for i in range(len(img)):
    for j in range(len(img[i])):
        newColor = s[getGrayColor(img[i][j])]
        ht[i][j] = newColor
        nh[newColor] += 1

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(ht)
plt.subplot(2, 2, 3)
plt.hist(h, 255, [0, 255])
plt.subplot(2, 2, 4)
plt.hist(nh, 255, [0, 255])

plt.show()
