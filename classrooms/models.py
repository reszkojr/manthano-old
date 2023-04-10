from django.db import models
from django.db.models import CASCADE

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    schedule = models.ImageField(upload_to='uploads/schedule_%Y_%m_%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Channel(models.Model):
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=100)

    classroom = models.ForeignKey('classrooms.Classroom', on_delete=CASCADE, default='', related_name='channels')

    def __str__(self):
        return self.name
    
    
