from turtle import title
from django.db import models
from django.forms import modelform_factory

# Create your models here.

JOB_TYPE = (
    ("Full time","Full time"),
    ("Part time","Part time"),
)

class job(models.Model):
    title = models.CharField(max_length=100, blank=True) # column
    # location
    job_type = models.CharField(max_length=20 , choices=JOB_TYPE)
    description = models.TextField(max_length=2000, default=None)
    published_time = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
        return self.title 

