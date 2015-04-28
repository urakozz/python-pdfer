from kozz.pdfer import Pdfer

__author__ = 'yury'


def main():

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