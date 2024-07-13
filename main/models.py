
# Create your models here.
# main/models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    signatures = models.IntegerField(default=0)

    def __str__(self):
        return self.title
