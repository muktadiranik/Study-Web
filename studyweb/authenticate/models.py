from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(
        upload_to="authenticate/users/images/", null=True, blank=True)
    bio = RichTextUploadingField(null=True, blank=True)
    skills = models.ManyToManyField(Skill)
