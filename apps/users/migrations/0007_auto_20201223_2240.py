# Generated by Django 3.1.4 on 2020-12-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201223_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='_media',
            new_name='social_media',
        ),
    ]