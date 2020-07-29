from django.contrib import admin
from .models import Files
from django import forms

admin.site.index_title="add files"
admin.site.site_title="BG-Portal"
admin.site.site_header="BG ADMIN PORTAL" 
     
class FilesAdmin(admin.ModelAdmin):
    list_display = ('name','id','last_updated_on','uploaded_file','updated_by')

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        obj.save() 

admin.site.register(Files,FilesAdmin)
