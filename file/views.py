from django.shortcuts import render
from .models import Files
from django.contrib.auth.models import User
from authority.models import Permission

def fileview(request):
    objectlist=[]
    u=request.user
    usrid=0
    m=User.objects.filter(username=u)
    for i in m:
        usrid=i.id
    print(usrid)    
    a=Permission.objects.filter(codename='change',user_id=usrid)
    for i in a:
        objectlist.append(i.object_id) 
    g=Files.objects.filter(id__in=objectlist)    
    print(g)    
    return render(request,'home.html')
