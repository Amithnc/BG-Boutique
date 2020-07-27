from django.shortcuts import render
from .models import Files
from django.contrib.auth.models import User
from authority.models import Permission
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/log')
def fileview(request):
    change_obj_id=[]
    view_obj_id=[]
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
