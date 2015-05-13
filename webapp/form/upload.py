import uuid
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from StringIO import StringIO

__author__ = 'yury'

from django import forms
from multiupload.fields import MultiFileField

class UploadForm(forms.Form):
    attachments = MultiFileField(max_num=30, min_num=1, max_file_size=100621440)
    bufferFiles = []

    def save(self):
        self.bufferFiles = []
        for each in self.cleaned_data['attachments']:
            buffer = self._handle_uploaded_file(each)
            self.bufferFiles.append(buffer)
            each.close()
        return self.bufferFiles

    def _handle_uploaded_file(self, f):
        if not isinstance(f, UploadedFile):
            raise Exception("invalid instance given: " + f.__class__.__name__)
        output = StringIO()
        for chunk in f.chunks():
            output.write(chunk)
        output.seek(0)
        return output

