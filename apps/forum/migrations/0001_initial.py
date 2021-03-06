# Generated by Django 3.1.4 on 2020-12-23 11:01

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(db_index=True, verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Name')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publish')),
                ('active', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Forums',
                'ordering': ('-publish',),
            },
        ),
    ]
