# Generated by Django 3.1.1 on 2020-12-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201203_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='car_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='career_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='collecting_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='food_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='health_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='meeting_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='other_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='technologies_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='tourism_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='travel_views',
            field=models.IntegerField(default=0),
        ),
    ]
