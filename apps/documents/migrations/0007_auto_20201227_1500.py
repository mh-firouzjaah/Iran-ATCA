# Generated by Django 3.1.4 on 2020-12-27 11:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20201227_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='document',
            name='subtitle_en',
        ),
        migrations.RemoveField(
            model_name='document',
            name='subtitle_fa',
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='document',
            name='description_fa',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='document',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publish'),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('article', 'Articles'), ('pdf', 'PDF'), ('video', 'Video'), ('voice', 'Voice'), ('other', 'Other file formats e.g: word, pptx,...')], default='no_file', max_length=50, verbose_name='Type'),
        ),
    ]