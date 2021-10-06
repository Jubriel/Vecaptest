from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
# Create your models here.
class Service(TenantMixin):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True

class Domain(DomainMixin):
    pass