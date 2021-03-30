from django.db import models
from django.urls import reverse

# Create your models here.


# 法、律、條例、通則
class Act(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    slug = models.SlugField(unique=True)
    source_url = models.URLField(default=None, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('acts')

    def __str__(self):
        return self.name


# 章
class Chapter(models.Model):
    act = models.ForeignKey(Act, on_delete=models.CASCADE, null=True, blank=False)
    number = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    source_url = models.URLField(default=None, null=True, blank=True)

    class Meta:
        ordering = ['act', 'number']

    def get_absolute_url(self):
        return reverse('act_detail', kwargs={'slug': self.act.slug})

    def __str__(self):
        return '第' + str(self.number) + '章 ' + str(self.name)

    def get_full_name(self):
        return self.act.__str__() + ' 第' + str(self.number) + '章 ' + str(self.name)


# 規程、規則、細則、辦法、綱要、標準、準則
class Regulations(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    source_url = models.URLField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name


# 條
class Article(models.Model):
    act = models.ForeignKey(Act, on_delete=models.CASCADE, null=True, blank=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.PositiveIntegerField(default=1, null=False, blank=False)
    number = models.CharField(max_length=5, null=False, blank=False)
    content = models.TextField()
    source_url = models.URLField(default=None, null=True, blank=True)
    termination = models.BooleanField(default=False)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['act', 'chapter', 'priority']

    def get_absolute_url(self):
        if self.chapter:
            return reverse('chapter_detail', kwargs={'slug': self.act.slug,
                                                     'number': self.chapter.number})
        else:
            return reverse('act_detail', kwargs={'slug': self.act.slug})

    def __str__(self):
        return '第' + str(self.number) + '條'

    def get_full_name(self):
        return self.act.__str__() + ' 第' + str(self.number) + '條'
