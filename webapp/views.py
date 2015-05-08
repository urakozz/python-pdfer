from kozz.pdfer import Pdfer
from webapp.form.upload import UploadForm
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View


# Create your views here.
def index(request):
    greetings = [{'when': "ta"}, {"when": "da"}]
    return render(request, 'index.html', {'greetings': greetings})


class IndexView(View):
    # template_name = "index.html"
    def get(self, request):
        greetings = [{'when': "ta"}, {"when": "da"}]
        form = UploadForm()
        return render(request, 'index.html', {'greetings': greetings, 'form': form})


class PdferView(View):
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return JsonResponse(form.errors)

        files = form.save()

        pdfer = Pdfer(files)
        pdfer.compress()
        pdfBytes = pdfer.getPdfBytes()

        # filePdf = open("name.pdf", "wb")
        # filePdf.write(pdfBytes)
        # filePdf.close()

        response = HttpResponse(pdfBytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="attach_compressed.pdf"'

        # return JsonResponse({"len": files.__len__()})
        return response
