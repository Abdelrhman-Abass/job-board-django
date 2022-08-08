from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.forms import modelform_factory
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.



JOB_TYPE = (
    ("Full time","Full time"),
    ("Part time","Part time"),
)

def image_upload(instance, filename):
    imagename , extension = filename.split('.')
    return "jobs/%s.%s"%(instance.id,extension)

class job(models.Model):
    owner = models.ForeignKey(User ,related_name='job_admin', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True) # column
    # location
    description = models.TextField(max_length=2000, default=None)
    job_type = models.CharField(max_length=20 , choices=JOB_TYPE)
    published_time = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    qualification = models.TextField(default='',max_length=4000,help_text='please put between lines  " , " ' )
    responsibility = models.TextField(default='', max_length=3000,help_text='please put between lines  " , " ')

    slug = models.SlugField(blank=True, null =True)

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super(job, self).save(*args,**kwargs)

    def __str__(self):
        return self.title 

class  category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class apply(models.Model):
    job = models.ForeignKey(job , related_name='apply_job', on_delete=models.CASCADE)

    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='upplay/') 
    
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



