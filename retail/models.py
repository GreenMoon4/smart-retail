from django.db import models

# Create your models here.
from django.db import models

class Products(models.Model):
    description = models.CharField(max_length=200)
    pricing = models.CharField(max_length=100)
    reviews = models.CharField(max_length=100)
    image = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'products'