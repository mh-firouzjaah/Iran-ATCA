# Generated by Django 3.1.4 on 2020-12-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_document_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
