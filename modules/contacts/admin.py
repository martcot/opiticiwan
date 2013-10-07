from contacts.models import *
from django.contrib import admin

class ConseillerAdmin(admin.ModelAdmin):
	list_display = ('nom', 'titre')
	
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'poste', 'tel', 'email')
	
admin.site.register(Conseiller,ConseillerAdmin)
admin.site.register(Contact,ContactAdmin)