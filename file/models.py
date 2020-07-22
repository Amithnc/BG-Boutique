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

class Master(models.Model):
    masters_file=models.FileField(upload_to='file',storage=OverwriteStorage(),help_text="please upload masters file")
    last_updated_on=models.DateTimeField(auto_now=True)
    updated_by= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,editable=False)

    def __str__(self):
        t=str(self.masters_file)
        return t[5:]   
class Sale(models.Model):
    sales_file=models.FileField(upload_to='file',storage=OverwriteStorage(),help_text="please upload sales file")
    last_updated_on=models.DateTimeField(auto_now=True)
    updated_by= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,editable=False)
    def __str__(self):
        t=str(self.sales_file)
        return t[5:] 