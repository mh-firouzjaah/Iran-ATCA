# Generated by Django 3.1.4 on 2021-01-06 09:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201226_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=250, verbose_name='Event')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('acknowledged', models.BooleanField(verbose_name='Acknowledged')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='users.airtrafficcontroller', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-created', '-updated'),
            },
        ),
    ]
