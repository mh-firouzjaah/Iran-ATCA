# Generated by Django 3.1.4 on 2020-12-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201223_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='link',
            field=models.URLField(verbose_name='Link'),
        ),
    ]
