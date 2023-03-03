#Name: Rio 
#Email:
#Date: 02-28-2023
#Program Description: asks for output name of image and creates an image of the number 6

import numpy as np
from matplotlib import pyplot as plt

outputName = input("Enter the name of the new image: ")

imageNew = np.zeros((30,30,3))
imageNew[:,:,0:2] = 1.0
imageNew[3:26,4:7,0:2] = 0.0
imageNew[13:16,4:26,0:2] = 0.0
imageNew[24:27,4:26,0:2] = 0.0
imageNew[15:27,23:26,0:2]= 0.0
imageNew[3:26,4:7,2] = 1.0
imageNew[13:16,4:26,2] = 1.0
imageNew[24:27,4:26,2] = 1.0
imageNew[15:27,23:26,2] = 1.0


#plt.imshow(imageNew)
#plt.show()
plt.imsave(outputName, imageNew)
