# Generated by Django 3.2 on 2022-08-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_auto_20220804_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='base/rooms/images/'),
        ),
    ]
