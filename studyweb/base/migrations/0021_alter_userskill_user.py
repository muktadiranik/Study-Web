# Generated by Django 3.2 on 2022-08-03 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_userskill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.userinfo'),
        ),
    ]
