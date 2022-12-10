from django.db import models

# Create your models here.

class UserInf(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

class BooksInf(models.Model):
    bname=models.CharField(max_length=64)
    bauthor=models.CharField(max_length=32)
    bimg=models.CharField(max_length=1024)
    bstate=models.CharField(max_length=32)