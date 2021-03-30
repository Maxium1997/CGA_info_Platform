from django.db import models

# Create your models here.

from law.models import Article


class Tag(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Case(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    notice = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    related_laws = models.ManyToManyField(Article)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
