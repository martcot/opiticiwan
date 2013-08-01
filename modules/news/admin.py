from news.models import *
from django.contrib import admin
	
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'lang')
	date_hierarchy = 'pub_date'
	
admin.site.register(News,NewsAdmin)

