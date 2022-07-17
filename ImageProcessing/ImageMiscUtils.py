import os
import cv2
import numpy as np


class ImageMiscUtils:
    @staticmethod
    def ResizeCV2Image(image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)

    @staticmethod
    def ResizeCV2ImageAtPath(path, width=None, height=None, inter=cv2.INTER_AREA):
        img = cv2.imread(path)
        return ImageMiscUtils.ResizeCV2Image(img, width, height, inter)
