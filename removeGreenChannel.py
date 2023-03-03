#Name: Rio
#Email: 
#Date: 02-25-2023
#Program Description: this program loads an image, displays it, and saves a new image with the green channel removed

import matplotlib.pyplot as plt
import numpy as np

imgName = input("Please enter the image path: ")
imgNameNew = input("Please enter new image name: ")

img = plt.imread(imgName)
plt.imshow(img)
#plt.show()

imgCopy = img.copy()
imgCopy[:,:,1] = 0

plt.imshow(imgCopy)
#plt.show()

plt.imsave(imgNameNew, imgCopy)
