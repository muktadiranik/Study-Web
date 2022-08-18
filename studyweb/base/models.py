from django.db import models
from authenticate.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, blank=True, related_name="participants")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="base/rooms/images/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-updated", "-created"]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = RichTextUploadingField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:255]
