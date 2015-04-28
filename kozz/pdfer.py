__author__ = 'yury'

import uuid
import os
import img2pdf
from PIL import Image
from PIL import ImageEnhance


class Pdfer:
    images = []
    size = (1500, 1500)
    invalidFiles = []
    outfiles = []

    def __init__(self, *images):
        if isinstance(images[0], list):
            images = images[0]
        self.images = images

    def setSize(self, size):
        self.size = size

    def compress(self):
        for filename in self.images:
            outfile = self.getTmpFileName(filename)
            try:
                image = Image.open(filename)
                image.thumbnail(self.size)
                converted = image.convert("L")
                converted = ImageEnhance.Contrast(converted).enhance(1.1)
                converted = ImageEnhance.Brightness(converted).enhance(1.1)
                converted = ImageEnhance.Sharpness(converted).enhance(1.4)
                converted.save(outfile, 'JPEG', optimize=True, progressive=True)
                self.outfiles.append(outfile)
            except IOError:
                self.invalidFiles.append(filename)
                pass
        return self

    def getPdfBytes(self):
        bytes = img2pdf.convert(self.outfiles)
        self.clearOutfiles()
        return bytes

    def getInvalidFiles(self):
        return self.invalidFiles

    def clearOutfiles(self):
        for filename in self.outfiles:
            os.remove(filename)

    def getTmpFileName(self, filename):
        fileNameSplit = os.path.splitext(filename)
        return "%s__%s.wb%s" % (fileNameSplit[0], uuid.uuid4().__str__(), fileNameSplit[1])



