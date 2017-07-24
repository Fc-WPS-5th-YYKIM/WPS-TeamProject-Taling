from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Lecture)
admin.site.register(Review)
admin.site.register(ClassLocation)
admin.site.register(LectureList)