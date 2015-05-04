import uuid
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

__author__ = 'yury'

from django import forms
from multiupload.fields import MultiFileField
from django.db import models


class ProfileImage(models.Model):
    image = models.FileField(upload_to='upload/')


class UploadForm(forms.Form):
    attachments = MultiFileField(max_num=30, min_num=1, max_file_size=30621440)
    somefiles = []

    def save(self, commit=True):

        for each in self.cleaned_data['attachments']:
            name = self._handle_uploaded_file(each)
            self.somefiles.append(name)

        return self.somefiles

    def _handle_uploaded_file(self, f):
        if not isinstance(f, InMemoryUploadedFile):
            raise Exception("invalid instance given")
        fileNameSplit = os.path.splitext(f.name)
        fname = "%s.tmp%s" % (uuid.uuid4().__str__(), fileNameSplit[1])
        with open(fname, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return fname

