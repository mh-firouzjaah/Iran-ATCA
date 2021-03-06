# Generated by Django 3.1.4 on 2020-12-26 10:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201223_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Body'),
        ),
    ]
