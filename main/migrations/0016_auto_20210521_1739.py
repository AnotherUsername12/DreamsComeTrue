# Generated by Django 3.1.5 on 2021-05-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_comment_comment_authorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biography',
            name='bio',
            field=models.CharField(default='Hello. I have not chosen my dream yet.', max_length=200),
        ),
    ]