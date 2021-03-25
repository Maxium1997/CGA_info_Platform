from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'source_url']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'act', 'number', 'name', 'source_url']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'act', 'chapter', 'number', 'source_url']
