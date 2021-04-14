from django.contrib import admin
from .models import cars
from django.utils.html import format_html
# Register your models here.

class Cars_Admin(admin.ModelAdmin):

    def thumbnail(self , object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.car_photo.url))

    thumbnail.short_description='car image'
    list_display = ('id','thumbnail','color','body_style','year','fuel_type','is_featured')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','body_style','color','city','fuel_type','year',)
    list_filter = ('body_style','fuel_type','color',)

admin.site.register(cars,Cars_Admin)
