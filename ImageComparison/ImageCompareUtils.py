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
