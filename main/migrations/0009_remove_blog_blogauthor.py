# Generated by Django 3.1.1 on 2020-12-10 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_person_visited_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blogauthor',
        ),
    ]
