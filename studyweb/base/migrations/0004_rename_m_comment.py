# Generated by Django 3.2 on 2022-08-02 01:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_rename_comment_m'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='M',
            new_name='Comment',
        ),
    ]
