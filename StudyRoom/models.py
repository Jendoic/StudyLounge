from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']
    @property
    def user_name(self):
        if self.name:
            return self.name
        return ''
   
    
    
class Topic(models.Model):
    name = models.CharField(max_length=200)
        
    def __str__(self):
        return str(self.name)
        
class Room(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participant = models.ManyToManyField(CustomUser, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_message', blank=True)
    
    class Meta:
        ordering = ['updated', 'created']
        
    def __str__(self):
        return self.body[:50]