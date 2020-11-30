# Generated by Django 3.1.3 on 2020-11-20 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News1', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 20, 20, 47, 50, 585825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='Author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='Title',
            field=models.CharField(max_length=25),
        ),
    ]
