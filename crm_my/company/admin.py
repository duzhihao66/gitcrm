from django.contrib import admin
from company import models
# Register your models here.

class Student(admin.ModelAdmin):
    list_display = ("id","name","birthday","qq","phone","room","course")
    list_display_links = ("id","name")


class Room(admin.ModelAdmin):
    list_display = ("id","city","area","name")
    list_display_links = ("id", "city")


class Course(admin.ModelAdmin):
    list_display = ("id","name", "intro", "cycle","lecturer")
    list_display_links = ("id", "name")


admin.site.register(models.Student,Student)
admin.site.register(models.Room,Room)
admin.site.register(models.Course,Course)








