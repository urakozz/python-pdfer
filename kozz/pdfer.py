__author__ = 'yury'

import uuid
import os
from PIL import Image
from PIL import ImageEnhance


class Pdfer:
    images = []
    size = (1500, 1500)
    outfiles = []

    def __init__(self, images, size=(1500, 1500)):
        self.images = images
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
                pass

    def getTmpFileName(self, filename):
        fileNameSplit = os.path.splitext(filename)
        return "%s__%s.wb%s" % (fileNameSplit[0], uuid.uuid4().__str__(), fileNameSplit[1])

