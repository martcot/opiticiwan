# -*- coding: utf-8 -*-
from django.contrib import admin, messages

from events.models import Event
	
class EventsAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	date_hierarchy = 'date'
	
admin.site.register(Event,EventsAdmin)