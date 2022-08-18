# Generated by Django 3.2 on 2022-08-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_userinfo_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]