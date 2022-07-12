import os
import cv2
import numpy as np


class ImageCompareUtils:
    @staticmethod
    def CompareImages(image1Path: str, image2Path: str, threshold: int) -> bool:
        img1 = cv2.imread(image1Path)
        img2 = cv2.imread(image2Path)
        diff = cv2.subtract(img1, img2)
        b, g, r = cv2.split(diff)
        nonZeroB = cv2.countNonZero(b)
        nonZeroG = cv2.countNonZero(g)
        nonZeroR = cv2.countNonZero(r)

        return nonZeroB <= threshold and nonZeroG <= threshold and nonZeroR <= threshold

    @staticmethod
    def GetDifferenceImage(image1Path: str, image2Path:str):
        img1 = cv2.imread(image1Path)
        img2 = cv2.imread(image2Path)
        absdiff = cv2.absdiff(img1, img2)
        gray = cv2.cvtColor(absdiff, cv2.COLOR_BGR2GRAY)

        for i in range(0, 3):
            dilated = cv2.dilate(gray.copy(), None, iterations=i+1)

        (temp, diff) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

        return diff
