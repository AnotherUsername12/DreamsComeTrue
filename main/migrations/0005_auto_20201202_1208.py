# Generated by Django 3.1.1 on 2020-12-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_person_dreamrubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='DreamRubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dreamrubric', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='dreamrubric',
        ),
        migrations.AddField(
            model_name='person',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.dreamrubric', verbose_name='Рубика'),
        ),
    ]