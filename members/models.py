from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
# from south.db import db
# from django.db.models.loading import cache

class artists(models.Model):
    firstname = models.CharField(max_length= 255, null = True)
    lastname = models.CharField(max_length= 255, null = True)
    email = models.EmailField(null = True)
    band = models.CharField(max_length=255, null=True)
    dateOfBirth = models.DateField(null=True)
    pp = models.FileField(null = True, upload_to='members/static/profile pics')
    coverphoto = models.FileField(null=True, upload_to='members/static/cover photos')
    bio = models.CharField(max_length=255, null=True)
    musicGenre = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "artists"

post_fields = {
    'media_post':models.FileField(null=True, upload_to='members/static/posts'),
    'text_post': models.CharField(max_length=255, null=True),
    'date_posted':models.DateField(null=True),
    'order':models.IntegerField(null=True),
    '__module__': 'members.models'
   }

# post = type('post', (models.Model,), post_fields)        
