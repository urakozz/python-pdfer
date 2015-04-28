from kozz.pdfer import Pdfer
import sys
import os
import uuid
import time
from simplejson import JSONEncoder
import img2pdf
from PIL import Image
from PIL import ImageEnhance

__author__ = 'yury'


def main():
    tStr = "someStr"
    print tStr

    # squares = [1, 4, 9, 16]
    size = (1500, 1500)
    print size

    files = ['IMG_2129.JPG', 'IMG_20130911_0026.jpg', 'image-05.jpg', "README.md"]

    pdfer = Pdfer(files)
    pdfBytes = pdfer.compress().getPdfBytes()
    invalidFiles = pdfer.getInvalidFiles()

    print invalidFiles

    filePdf = open("name.pdf", "wb")
    filePdf.write(pdfBytes)
    filePdf.close()


if __name__ == '__main__':
    main()