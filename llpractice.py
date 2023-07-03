# Importing libraries
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import cv2

imageDir = 'images/'
imageFiles = os.listdir(imageDir)
imageList = []
for i in range(0, len(imageFiles)):
    imageList.append(mpimg.imread(imageFiles[i]))
print(imageFiles)