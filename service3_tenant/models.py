from django.db import models
from django.db.models.base import Model

from service3_shared.models import service3Type

# Create your models here.
class service3(models.Model):
    service3_type = models.ForeignKey(service3Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=200, default='SOME STRING')
    
