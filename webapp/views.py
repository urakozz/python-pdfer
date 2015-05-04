import uuid
from kozz.pdfer import Pdfer
import os
from webapp.form.upload import UploadForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.
def index(request):
    # return HttpResponse('Hello !')
    greetings = [{'when': "ta"}, {"when": "da"}]
    return render(request, 'index.html', {'greetings': greetings})


class IndexView(View):
    # template_name = "index.html"
    def get(self, request):
        greetings = [{'when': "ta"}, {"when": "da"}]
        form = UploadForm()
        return render(request, 'index.html', {'greetings': greetings, 'form': form})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse(form.errors.as_json())

        files = []
        for filename, file in request.FILES.iteritems():
            name = request.FILES[filename].name
            chunks = request.FILES[filename].chunks()
            fname = self._handle_uploaded_file(chunks, name)
            files.append(fname)

        pdfer = Pdfer(files)
        pdfBytes = pdfer.compress().getPdfBytes()
        invalidFiles = pdfer.getInvalidFiles()
        pdfer.removeOriginals().clearOutfiles()

        print invalidFiles

        filePdf = open("name.pdf", "wb")
        filePdf.write(pdfBytes)
        filePdf.close()

        return HttpResponse(invalidFiles.__str__())

    def _handle_uploaded_file(self, f, name):
        fileNameSplit = os.path.splitext(name)
        fname = "%s.%s" % (uuid.uuid4().__str__(), fileNameSplit[1])
        with open(fname, 'wb+') as destination:
            for chunk in f:
                destination.write(chunk)
        return fname
