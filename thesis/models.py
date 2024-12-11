from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone




class medpapers(models.Model):
    Title = models.CharField(max_length=100)
    Authors = models.CharField(max_length=100)
    Abstract = models.TextField()
    tags = TaggableManager()
    
    def __str__(self):
        return self.Title

class itpapers(models.Model):
    Title = models.CharField(max_length=100)
    Authors = models.CharField(max_length=100)
    Abstract = models.TextField()
    tags = TaggableManager()
    
    def __str__(self):
        return self.Title
    
class cspapers(models.Model):
    Title = models.CharField(max_length=100)
    Authors = models.CharField(max_length=100)
    Abstract = models.TextField()
    tags = TaggableManager()
    
    def __str__(self):
        return self.Title
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    post = models.ForeignKey('medpapers', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Comment by {self.name}"
    
class itcomment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    post = models.ForeignKey('itpapers', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Comment by {self.name}"
    
class cscomment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    post = models.ForeignKey('cspapers', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Comment by {self.name}"
    
