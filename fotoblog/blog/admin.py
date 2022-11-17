from django.contrib import admin
from .models import Photo,Blog

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image','uploader']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', ]