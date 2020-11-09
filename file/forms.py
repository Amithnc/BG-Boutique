from django import forms  
from .models import Files  
from django.http import JsonResponse
from django.http import HttpResponse
class FilesForm(forms.ModelForm):  
    class Meta:  
        model = Files  

        fields = ('uploaded_file',)  
        help_texts = {
            'uploaded_file': '',
        }
    def clean(self):    
        new=self.cleaned_data['uploaded_file']  
        new=str(new)  
        f=str(self.instance.uploaded_file)  
        f=f[5:]
        print(new,f)
        if new!=f:
            print("hi")
            return JsonResponse({"message":"**WRONG FILE !**  Please Make sure that you are updating the same file as above mentioned"},status_code=400)
            # return HttpResponse('**WRONG FILE !**  Please Make sure that you are updating the same file as above mentioned')
        return self.cleaned_data

class FilesFormnovalidate(forms.ModelForm):  
    class Meta:  
        model = Files  
        fields = ('uploaded_file',)  
        help_texts = {
            'uploaded_file': '',
        }  
             