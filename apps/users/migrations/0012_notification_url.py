# Generated by Django 3.1.4 on 2021-01-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210106_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.URLField(default='', verbose_name='URL'),
            preserve_default=False,
        ),
    ]
