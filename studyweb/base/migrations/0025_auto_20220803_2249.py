# Generated by Django 3.2 on 2022-08-03 16:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20220803_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
