# Generated by Django 3.1.1 on 2020-11-24 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(default='Hello. I use ToDo app.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribes', models.IntegerField(default=0)),
                ('subscribed', models.TextField(default='Z')),
                ('biography', models.CharField(default='Hello. I use ToDo app.', max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_field', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('music', models.FileField(blank=True, null=True, upload_to='', verbose_name='Музыка')),
                ('visible', models.BooleanField(blank=True, default=True)),
                ('author', models.CharField(default='User', max_length=30)),
                ('authorid', models.TextField(default='z')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('done', models.CharField(default='Не выполнено', max_length=30)),
                ('views', models.IntegerField(default=0)),
                ('viewers', models.TextField(default='Z')),
                ('tauthor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tauthor', to='main.person')),
            ],
        ),
    ]
