# Generated by Django 3.1.1 on 2020-12-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_blog_blogauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='subscribed',
            field=models.TextField(default='0'),
        ),
    ]
