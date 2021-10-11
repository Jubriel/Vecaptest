from django.contrib import admin

# Register your models here.
from service3_shared.models import service3Type

@admin.register(service3Type)
class service3TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)