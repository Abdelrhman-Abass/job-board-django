from tabnanny import verbose
from django.db import models

# Create your models here.
class info(models.Model):

    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    class Meta: 
        verbose_name = ('info')
        verbose_name_plural = ('info')

    def __str__(self):
        return self.email


    
