from django.db import models


# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Movie Description')
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Category Description')
    movies_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Cast(models.Model):
    the_hero_name = models.CharField(max_length=255)
    director_name = models.CharField(max_length=255)
    cameraman_name = models.CharField(max_length=255)

    def __str__(self):
        return self.the_hero_name
