from django.contrib import admin

from .models import Blog, Person, DreamRubric, Comment

# Register your models here.

admin.site.register(Blog)
admin.site.register(Person)
admin.site.register(DreamRubric)
admin.site.register(Comment)