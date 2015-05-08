__author__ = 'yury'

import uuid
import os
import img2pdf
import threading
import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageEnhance
from skimage.filters import threshold_adaptive
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from StringIO import StringIO
import matplotlib
from matplotlib.image import pil_to_array


class Pdfer:
    images = None
    size = (1500, 1500)
    invalidFiles = []
    tmp_files = []
    outfiles = None

    _dpi = 100

    _removeOriginalImages = False

    def __init__(self, *images):
        if isinstance(images[0], list):
            images = images[0]
        self.images = []
        self.outfiles = []
        for buffer in images:
            self.addImage(buffer)
        plt.gray()

    def addImage(self, buffer):
        if not isinstance(buffer, StringIO):
            raise Exception("wrong image instance given")
        self.images.append(buffer)

    def setSize(self, size):
        self.size = size

    def compress(self):
        processStack = []
        for fileBuffer in self.images:
            # self.processImage(fileBuffer)
            process = threading.Thread(target=self.processImage, args=[fileBuffer])
            process.start()
            processStack.append(process)
        for process in processStack:
            process.join()
        return self

    def processImage(self, fileBuffer):
        # tmp_name = uuid.uuid4().__str__() + ".png"
        # try:

        image = Image.open(fileBuffer)
        image.thumbnail(self.size)
        converted = image.convert("L")
        # converted = ImageEnhance.Contrast(converted).enhance(1.1)
        # converted = ImageEnhance.Brightness(converted).enhance(1.1)
        converted = ImageEnhance.Sharpness(converted).enhance(1.4)
        # fileBuffer.close()

        # image = np.array(converted)
        image = matplotlib.image.pil_to_array(converted)
        binary_adaptive = threshold_adaptive(image, 40, offset=10)

        figsize = [x / float(self._dpi) for x in (binary_adaptive.shape[1], binary_adaptive.shape[0])]
        fig = Figure(figsize=figsize, dpi=self._dpi, frameon=False)
        canvas = FigureCanvasAgg(fig)
        fig.figimage(binary_adaptive)

        output = StringIO()
        fig.savefig(output, format='png')
        output.seek(0)
        #

        # with open(tmp_name, "wb") as file:
        #     file.write(output.getvalue())
        #     file.close()
        # output.close()


        self.outfiles.append(output)
        # except IOError:
        #     self.invalidFiles.append(fileBuffer)
        #     pass

    def getPdfBytes(self):
        bytes = img2pdf.convert(self.outfiles)
        return bytes





