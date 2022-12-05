from django.contrib import admin
from .models import  Contact, Service, Donate, About, Ourvision, Ourmission, Ourvalues, Donatebanner, Enoughdonate

admin.site.register(Service) 
admin.site.register(Donate) 
admin.site.register(About) 
admin.site.register(Ourvision) 
admin.site.register(Ourmission) 
admin.site.register(Ourvalues) 
admin.site.register(Donatebanner) 
admin.site.register(Enoughdonate) 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'email')
    list_display_links = ('id', 'fullname',)
    search_fields = ('fullname', 'phone', 'email')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin) 
