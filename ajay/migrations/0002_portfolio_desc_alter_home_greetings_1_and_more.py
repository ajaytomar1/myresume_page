# Generated by Django 4.1.2 on 2022-11-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=10),
        ),
    ]
