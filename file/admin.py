from django.contrib import admin
from .models import Master,Sale
admin.site.index_title="add files"
admin.site.site_title="BG-Portal"
admin.site.site_header="Log in to BG"

class MasterAdmin(admin.ModelAdmin):
    list_display = ('last_updated_on','masters_file','updated_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        obj.save() 
class SaleAdmin(admin.ModelAdmin):
    list_display = ('last_updated_on','sales_file','updated_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        obj.save()         
admin.site.register(Master,MasterAdmin)
admin.site.register(Sale,SaleAdmin)