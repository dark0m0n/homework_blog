from django.contrib import admin
from news.models import Article

# Register your models here.
@admin.register(Article)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'text']
