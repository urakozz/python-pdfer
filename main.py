import time
import threading
import StringIO
from kozz.pdfer import Pdfer

__author__ = 'yury'


def run_pdfer():
    # files = ['Scan_DiplomaRus.jpeg', 'Scan_RefLetter.jpeg', "IMG_2129.JPG"]
    files = ["i24-bonitaetscheck.pdf"]
    streams = []
    for file in files:
        stream = StringIO.StringIO()
        with open(file) as s:
            stream.write(s.read())
        streams.append(stream)

    pdfer = Pdfer(streams)
    pdfBytes = pdfer.compress().getPdfBytes()

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