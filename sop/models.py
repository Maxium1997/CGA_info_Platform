from django.db import models

# Create your models here.

from law.models import Article


class Case(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    related_laws = models.ManyToManyField(Article)
    notice_items = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
