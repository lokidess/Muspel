from django.contrib import admin
from Course.models import Course, Comment, Category, Lecture

# Register your models here.
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Lecture)
