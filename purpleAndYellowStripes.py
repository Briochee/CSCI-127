#Name: Rio
#Email: 
#Date: 02-28-2023
#Program Description: asks for dimensions, creates image with purple and yellow stripes

import numpy as np
from matplotlib import pyplot as plt

dimn = int(input("Enter Dimensions: "))

pyImage = np.ones((dimn, dimn,3))
pyImage[0::2,:,1] = 0.0
pyImage[1::2,:,2] = 0.0

#plt.imshow(pyImage)
#plt.show()
plt.imsave("stripes.png", pyImage)
