from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)