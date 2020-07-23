from django.contrib import admin
from .models import Master,Sale
from django import forms
admin.site.index_title="add files"
admin.site.site_title="BG-Portal"
admin.site.site_header="Log in to BG"

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = '__all__'
    def clean_masters_file(self):
        n = self.cleaned_data.get('masters_file')
        name=str(self.cleaned_data.get('masters_file'))
        search=['Master','master','masters','Masters']
        t=''
        for i in name:
            t=t+i
            if t in search:
                return n 
        else:
            raise forms.ValidationError("cant upload files other than Masters")  
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
    def clean_sales_file(self):
        n = self.cleaned_data.get('sales_file')
        name=str(self.cleaned_data.get('sales_file'))
        search=['Sales','sales',]
        t=''
        for i in name:
            t=t+i
            if t in search:
                return n 
        else:
            raise forms.ValidationError("cant upload files other than sales")        
class MasterAdmin(admin.ModelAdmin):
    list_display = ('last_updated_on','masters_file','updated_by')

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        obj.save() 
    form = MasterForm    
class SaleAdmin(admin.ModelAdmin):
    list_display = ('last_updated_on','sales_file','updated_by')
    form = SaleForm
    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        obj.save()         
admin.site.register(Master,MasterAdmin)
admin.site.register(Sale,SaleAdmin)