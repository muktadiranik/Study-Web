# Generated by Django 3.2 on 2022-08-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_userimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(upload_to='base/user/image/'),
        ),
    ]
