__author__ = 'yury'

import uuid
import os
import img2pdf
import threading
import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageEnhance
from skimage import io
from skimage.filters import threshold_adaptive


class Pdfer:
    images = []
    size = (1500, 1500)
    invalidFiles = []
    tmp_files = []
    outfiles = []

    _removeOriginalImages = False

    def __init__(self, *images):
        if isinstance(images[0], list):
            images = images[0]
        self.images = images
        plt.gray()

    def setSize(self, size):
        self.size = size

    def compress(self):
        processStack = []
        for filename in self.images:
            process = threading.Thread(target=self.processImage, args=[filename])
            process.start()
            processStack.append(process)
        for process in processStack:
            process.join()
        return self

    def processImage(self, filename):
        outfile = self.getTmpFileName(filename)
        tmp_name = uuid.uuid4().__str__() + ".png"
        try:
            image = Image.open(filename)
            image.thumbnail(self.size)
            converted = image.convert("L")
            # converted = ImageEnhance.Contrast(converted).enhance(1.1)
            # converted = ImageEnhance.Brightness(converted).enhance(1.1)
            converted = ImageEnhance.Sharpness(converted).enhance(1.4)
            converted.save(tmp_name, 'PNG')

            image = io.imread(tmp_name)
            binary_adaptive = threshold_adaptive(image, 40, offset=10)

            plt.imsave(outfile, binary_adaptive)

            self.outfiles.append(outfile)
            self.tmp_files.append(tmp_name)
        except IOError:
            self.invalidFiles.append(filename)
            pass

    def getPdfBytes(self):
        bytes = img2pdf.convert(self.outfiles)
        self.clearOutfiles()
        return bytes

    def getInvalidFiles(self):
        return self.invalidFiles

    def clearOutfiles(self):
        threads = []
        for filename in self.toDelete():
            thread = threading.Thread(target=os.remove, args=[filename])
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    def toDelete(self):
        for filename in self.outfiles:
            yield filename
        for filename in self.tmp_files:
            yield filename
        if self._removeOriginalImages:
            for filename in self.images:
                yield filename

    def removeOriginals(self):
        self._removeOriginalImages = True
        return self

    def getTmpFileName(self, filename):
        fileNameSplit = os.path.splitext(filename)
        return "%s__%s.wb%s.png" % (fileNameSplit[0], uuid.uuid4().__str__(), fileNameSplit[1])



