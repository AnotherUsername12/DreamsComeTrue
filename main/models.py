from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE)
    subscribes = models.IntegerField(default = 0)
    subscribed = models.TextField(default = 'Z')
    dream = models.CharField(max_length = 50, default = '')
    biography = models.CharField(max_length = 200, default = 'Hello. I have not chosen my dream yet.')
    email = models.EmailField(default = '')
    rubric = models.CharField(max_length = 100, default = '')
    
    stringid = models.TextField(default = 'Z')
    
    visited_profile = models.TextField(default = 'Z')
    
    tourism_views = models.IntegerField(default = 0)
    travel_views = models.IntegerField(default = 0)
    technologies_views = models.IntegerField(default = 0)
    car_views = models.IntegerField(default = 0)
    food_views = models.IntegerField(default = 0)
    collecting_views = models.IntegerField(default = 0)
    career_views = models.IntegerField(default = 0)
    health_views = models.IntegerField(default = 0)
    meeting_views = models.IntegerField(default = 0)
    other_views = models.IntegerField(default = 0)

    
class DreamRubric(models.Model):
    drubric = models.CharField(max_length = 100, db_index = True)
    
    def __str__(self):
        return self.drubric
    
    
@receiver(post_save, sender=User)
def create_user_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_person(sender, instance, **kwargs):
    instance.person.save()

    
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    text = models.CharField(max_length = 500)
    image = models.ImageField(verbose_name = 'Изображение', null = True, blank = True)
    author = models.CharField(max_length = 30, default = 'User')
    authorid = models.TextField(default = 'z')
    published = models.DateTimeField(auto_now_add = True, db_index = True)
    views = models.IntegerField(default = 0)
    viewers = models.TextField(default = 'Z')
    
    
class Comment(models.Model):
    comment_text = models.CharField(max_length = 150)
    comment_author = models.CharField(max_length = 30, default = 'User')
    comment_authorid = models.TextField(default = 'z')
    comment_published = models.DateTimeField(auto_now_add = True, db_index = True)
    comment_blogid = models.TextField(default = 'z')
    publicationcomment = models.ForeignKey('Blog', null = True, blank = True, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment_text
    
    
class Search(models.Model):
    search_field = models.CharField(max_length = 100)
    
    
class Biography(models.Model):
    bio = models.CharField(max_length = 200, default = 'Hello. I have not chosen my dream yet.')
    dream = models.CharField(max_length = 50, default = '')
    rubric = models.ForeignKey('DreamRubric', null = True, on_delete=models.PROTECT, verbose_name='Рубика')
    dreamrubric = models.CharField(max_length = 100, default = '')
    
    
class Email(models.Model):
    email = models.EmailField(default = '')