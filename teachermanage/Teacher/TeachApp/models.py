from distutils.command.upload import upload
import uuid
from django.db import models


class alwin(models.Model):
    hii = models.CharField(max_length=12)


class Cobra(models.Model):
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class signup(models.Model):
    Name = models.CharField(max_length=30)
    UserName = models.CharField(unique=True,max_length=10)
    Password = models.CharField(max_length=20)
    Confirm_Password = models.CharField(max_length=20)
    Code = models.CharField(primary_key=True,max_length=12)

    def __str__(self):
        return self.UserName


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return f'{self.name} Profile'

class master(models.Model):
    uname= models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    name = models.CharField(primary_key=True,max_length=20)
    photo = models.ImageField(upload_to='media')
    dob = models.DateField()
    qualification = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    address = models.TextField()
    UG =models.IntegerField()
    ugfile = models.FileField(upload_to="media")
    PG =models.IntegerField()
    pgfile = models.FileField(upload_to="media")
    Mphil =models.IntegerField()
    mphilgfile = models.FileField(upload_to="media")
    Phd =models.IntegerField()
    phdfile = models.FileField(upload_to="media")
    ex =models.IntegerField()
    exfile = models.FileField(upload_to="media")
    research_paper = models.URLField()
    net =models.IntegerField()
    netfile = models.FileField(upload_to="media")
    set = models.IntegerField()
    setfile = models.FileField(upload_to="media")
    jrf =models.IntegerField()
    jrffile = models.FileField(upload_to="media")
    jrfdate = models.DateField()
    award =models.CharField(max_length=100)
    awardfile = models.FileField(upload_to="media")

    def __str__(self):
        return f'{self.name} Profile'

class score(models.Model):
    name = models.CharField(max_length=20)
    api = models.IntegerField()
