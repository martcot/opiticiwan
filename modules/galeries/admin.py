from galeries.models import *
from django.contrib import admin

class PhotoTitleInline(admin.TabularInline):
	model = PhotoTitle
	extra = 1
	
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('photo',)
	inlines = (PhotoTitleInline,)	

class PhotoInline(admin.TabularInline):
	model = Photo.album.through
	extra = 1
	
class GalerieAdmin(admin.ModelAdmin):
	list_display = ('title', 'lang')
	inlines = (PhotoInline,)	
	
admin.site.register(Gallery, GalerieAdmin)
admin.site.register(Photo, PhotoAdmin)
