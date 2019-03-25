from django.contrib import admin

# Register your models here.
from .models import Productwithimage, photoframe


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	search_fields = ['title','description']
	list_display = ['title','price','updated']
	list_editable = ['price']
	list_filter = ['price']
	readonly_field = ['updated','timestamp']
	prepopulated_fields = {"slug": ("title",)}

class photoframeAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	search_fields = ['title','description']
	list_display = ['title','price','updated']
	list_editable = ['price']
	list_filter = ['price']
	readonly_field = ['updated','timestamp']
	prepopulated_fields = {"slug": ("title",)}
 	
	

admin.site.register(Productwithimage, ProductAdmin)

admin.site.register(photoframe, photoframeAdmin)