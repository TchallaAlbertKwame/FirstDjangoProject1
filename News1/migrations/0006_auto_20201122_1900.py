# Generated by Django 3.1.3 on 2020-11-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News1', '0005_auto_20201121_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnews',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sportnews',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
