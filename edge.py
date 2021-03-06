import cv2
import numpy as np
def strokeEdges(src,dst,blurKsize=7,edgeKsize=5):
    if blurKsize>=3:
        blurredSrc=cv2.medianBlur(src,blurKsize)
        graySrc=cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize=edgeKsize)
    normalizedInverseAlpha=(1.0/255)*(255-graySrc)
    channels=cv2.split(src)
    for channel in channels:
        channel[:]=channel*normalizedInverseAlpha
    cv2.merge(channels,dst)
image=cv2.imread('C:\\Users\\neil\\Downloads\\cm.jpg')
image2=cv2.imread('C:\\Users\\neil\\Downloads\\cm.jpg')
strokeEdges(image,image2)
cv2.imshow('new',image2)
