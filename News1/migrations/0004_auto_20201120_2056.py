# Generated by Django 3.1.3 on 2020-11-20 20:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News1', '0003_auto_20201120_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 20, 20, 56, 30, 19131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 20, 20, 56, 30, 190108, tzinfo=utc)),
        ),
    ]
