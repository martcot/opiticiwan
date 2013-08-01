from polls.models import *
from django.contrib import admin
	
class ChoicesInline(admin.TabularInline):
	model = PollChoices
	extra = 2
	
class PollsAdmin(admin.ModelAdmin):
	list_display = ('question', 'pub_date', 'lang')
	date_hierarchy = 'pub_date'
	inlines = (ChoicesInline,)	
	
admin.site.register(Poll,PollsAdmin)

