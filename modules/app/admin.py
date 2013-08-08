from app.models import *
from django.contrib import admin
	
class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'courriel', 'sub_date')
	date_hierarchy = 'sub_date'
	
admin.site.register(Subscription,SubscriptionAdmin)

