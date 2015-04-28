import time
import threading
from kozz.pdfer import Pdfer

__author__ = 'yury'


def run_pdfer():
    files = ['IMG_2129.JPG', 'IMG_20130911_0026.jpg', 'image-05.jpg', "README.md"]

    pdfer = Pdfer(files)
    pdfBytes = pdfer.compress().getPdfBytes()
    invalidFiles = pdfer.getInvalidFiles()

    print invalidFiles

    filePdf = open("name.pdf", "wb")
    filePdf.write(pdfBytes)
    filePdf.close()


def main():
    thr = threading.Thread(target=run_pdfer, args=(), kwargs={})
    thr.start()

    while thr.isAlive():
        for s in ["|", "/", "-", "\\"]:
            print "%s\r\b" % s
            time.sleep(0.05)
    # thr.join()
    print "end"

    exit(0)


if __name__ == '__main__':
    main()