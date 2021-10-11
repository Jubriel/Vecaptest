from django.contrib import admin

# Register your models here.
from service3_tenant.models import service3

@admin.register(service3)
class service3Admin(admin.ModelAdmin):
    list_display = ('name',)
    