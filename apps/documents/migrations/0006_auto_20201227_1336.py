# Generated by Django 3.1.4 on 2020-12-27 10:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20201226_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='document',
            name='description_fa',
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.URLField(blank=True, help_text='If file is uploaded on hosts', null=True, verbose_name='Download link'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('video', 'Video'), ('pdf', 'PDF'), ('voice', 'Voice'), ('no_file', 'Text messages'), ('other', 'Other file formats e.g: word, pptx,...')], default='no_file', max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='documentcategory',
            name='title',
            field=models.CharField(db_index=True, help_text='categories e.g: Education, ATC docs,...', max_length=250, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='documentcategory',
            name='title_en',
            field=models.CharField(db_index=True, help_text='categories e.g: Education, ATC docs,...', max_length=250, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='documentcategory',
            name='title_fa',
            field=models.CharField(db_index=True, help_text='categories e.g: Education, ATC docs,...', max_length=250, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
    ]
