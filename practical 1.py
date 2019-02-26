import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('light.jpeg',0)#o indicate grayscaled color while 1 indicates colored picture
cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
