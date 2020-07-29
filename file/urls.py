from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.fileview,name='home'),
    path('log/',
        LoginView.as_view(
            template_name='admin/login.html',
            extra_context={
                'site_header': 'Log in to BG',
                'site_title' : 'BG-Portal',
            })),
    path('log-out/',views.logout),
    path('update/<int:id>/', views.update,name='update'),
    path('viewfile/',views.viewfiles,)
]    
    
