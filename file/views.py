from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Files
from django.contrib.auth.models import User
from authority.models import Permission
from django.contrib import auth
from .forms import FilesForm 
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import urllib



@login_required(login_url='/log')
def fileview(request):
    view_obj_id=[]
    change_obj_id=[]
    u=request.user
    usrid=0
    m=User.objects.filter(username=u)
    for i in m:
        usrid=i.id  
    a=Permission.objects.filter(codename='change',user_id=usrid)
    b=Permission.objects.filter(codename='view',user_id=usrid)
    for i in a:
        change_obj_id.append(i.object_id)     
    for i in b:
        view_obj_id.append(i.object_id) 

    filteredchange=Files.objects.filter(id__in=change_obj_id)
    filteredview=Files.objects.filter(id__in=view_obj_id)
    context={}
    context['view']=filteredview
    context['changes']=filteredchange
    return render(request,'home.html',context)

def logout(request):
    auth.logout(request)
    return render(request,'logagain.html')

def update(request, id):  
    instance = get_object_or_404(Files,id=id)  
    form = FilesForm(request.POST  or None,files=request.FILES,instance = instance)  
    if request.method == "POST":
        if form.is_valid():
            profile = form.save(commit=False)
            profile.updated_by=request.user
            profile.save()
            return redirect("/")
    context={}
    context['instance']=instance  
    context['form']=form  

    return render(request,'update.html',context)   

def viewfiles(request):
    context={ }
    obj_id=request.POST.get('viewfiles',None)
    viewfile=Files.objects.filter(id=int(obj_id))
    for i in viewfile:
        url=i.uploaded_file
    print(url)    
    context['url']='/media/'+str(url)
    return render(request,'view.html',context)

