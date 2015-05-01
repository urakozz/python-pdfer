import time
import threading
import django
from kozz.pdfer import Pdfer

__author__ = 'yury'


def run_pdfer():
    files = ['Scan_DiplomaRus.jpeg', 'Scan_RefLetter.jpeg', "IMG_2129.JPG", "README.md"]

    pdfer = Pdfer(files)
    pdfBytes = pdfer.compress().getPdfBytes()
    invalidFiles = pdfer.getInvalidFiles()

    print invalidFiles

    filePdf = open("name.pdf", "wb")
    filePdf.write(pdfBytes)
    filePdf.close()


def main():
    print django.get_version();
    exit(0);
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