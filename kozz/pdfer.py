from wand.exceptions import MissingDelegateError, WandException

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
from wand.image import Image as WandImage
from wand.color import Color



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
        matplotlib.use('Agg')

    def addImage(self, buffer):
        if not isinstance(buffer, StringIO):
            raise Exception("wrong image instance given")
        self.preProcessImage(buffer)

    def setSize(self, size):
        self.size = size

    def compress(self):
        processStack = []
        for fileBuffer in self.images:
            self.processImage(fileBuffer)
            # process = threading.Thread(target=self.processImage, args=[fileBuffer])
            # process.start()
            # processStack.append(process)
        for process in processStack:
            process.join()
        return self

    def preProcessImage(self, buffer):
        try:
            with WandImage(blob=buffer.getvalue(), resolution=150) as img_seq:
                for img in img_seq.sequence:
                    with WandImage(width=img.width, height=img.height, background=Color("white")) as bg:
                        bg.composite(img,0,0)
                        blob = bg.make_blob('png')
                        self.images.append(StringIO(blob))
        except MissingDelegateError:
            self.images.append(buffer)


    def processImage(self, fileBuffer):
        # tmp_name = uuid.uuid4().__str__() + ".png"
        try:

            image = Image.open(fileBuffer)
            image.thumbnail(self.size)
            converted = image.convert("L")
            # converted = ImageEnhance.Contrast(converted).enhance(1.1)
            # converted = ImageEnhance.Brightness(converted).enhance(1.1)
            converted = ImageEnhance.Sharpness(converted).enhance(1.4)

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

            self.outfiles.append(output)
        except IOError:
            self.invalidFiles.append(fileBuffer)

    def getPdfBytes(self):
        bytes = img2pdf.convert(self.outfiles)
        return bytes





