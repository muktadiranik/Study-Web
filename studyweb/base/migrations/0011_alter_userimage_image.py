# Generated by Django 3.2 on 2022-08-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20220803_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
