from django.contrib import admin
from .models import Mark

# Register your models here.
@admin.register(Mark)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'subject', 'mark']