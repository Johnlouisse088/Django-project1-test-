from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    room = models.CharField(max_length=255, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.room

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, null=True)


