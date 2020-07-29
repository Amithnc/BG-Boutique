from django.shortcuts import render,get_object_or_404,redirect
from .models import Files
from django.contrib.auth.models import User
from authority.models import Permission
from django.contrib import auth
from .forms import FilesForm 
from django.contrib.auth.decorators import login_required
from django.db.models import Q




@login_required(login_url='/log')
def fileview(request):
    if request.user.is_superuser:
        filteredchange=Files.objects.all()
        filteredview=Files.objects.all()
    else:
        view_obj_id=[]
        change_obj_id=[]
        u=request.user
        usrid=0
        m=User.objects.filter(username=u)
        for i in m:
            usrid=i.id  
        a=Permission.objects.filter(Q(codename='change')|Q(codename='change&view'),user_id=usrid,approved=1)
        b=Permission.objects.filter(Q(codename='view')|Q(codename='change&view'),user_id=usrid,approved=1)
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


