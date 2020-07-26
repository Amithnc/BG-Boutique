from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name,max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Files(models.Model):
    uploaded_file=models.FileField(upload_to='file',storage=OverwriteStorage(),help_text="please upload file",verbose_name='file')
    last_updated_on=models.DateTimeField(auto_now=True)
    updated_by= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,editable=False)
    name=models.CharField(max_length=30,default='',blank=False,editable=False,help_text="this field will be auto poluted")

    def save(self, *args, **kwargs):
        extracted_name=str(self.uploaded_file)
        extracted_name=extracted_name.split('.')
        self.name=extracted_name[0]
        super(Files, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name) 

    class Meta:
        verbose_name_plural = "files"