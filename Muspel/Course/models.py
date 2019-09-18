from django.db import models
from embed_video.fields import EmbedVideoField


class Course(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey('Course.Category', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('Course.Comment', on_delete=models.CASCADE, null=True, blank=True)
    status_course = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Lecture(models.Model):
    name_lecture = models.CharField(max_length=255)
    text_lecture = models.TextField()
    home_work = models.TextField()
    lecture_status = models.BooleanField(default=False)
    video = EmbedVideoField(blank=True, verbose_name='Видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_lecture



