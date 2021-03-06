import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', 0)
canny = cv.Canny(img,100, 200) # if a pixel gradient is higher than upper threshold, pixel is accepted as edge.
                               # if a pixel gradient value is below the lower threshold, then it is rejected.


images = [img, canny]
titles = ['img', 'canny']
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()