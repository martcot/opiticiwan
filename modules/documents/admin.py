from documents.models import *
from django.contrib import admin

class DocsInline(admin.TabularInline):
	model = Document.category.through
	extra = 1
	
class DocumentsCategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'lang')
	inlines = (DocsInline,)
	
class DocumentsAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'lang')
	date_hierarchy = 'pub_date'

admin.site.register(Category,DocumentsCategoryAdmin)
admin.site.register(Document,DocumentsAdmin)

