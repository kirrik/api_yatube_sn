# Generated by Django 3.0.5 on 2020-04-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200422_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='URL'),
        ),
    ]
