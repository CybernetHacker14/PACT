import os
import cv2
import tkinter
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

    @staticmethod
    def OpenImageInWindow(
        path: str, windowname: str, fitToScreen: bool, width=None, height=None
    ):
        image = cv2.imread(path)
        root = tkinter.Tk()
        root.withdraw()

        if fitToScreen:
            image = ImageMiscUtils.ResizeCV2Image(
                image,
                root.winfo_screenwidth() if width is None else width,
                root.winfo_screenheight() if height is None else height,
            )

        cv2.imshow(windowname, image)
        key = cv2.waitKey(0)
        return windowname, key
