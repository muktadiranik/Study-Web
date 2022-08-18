from django.contrib import admin
from django.contrib.admin import TabularInline
from . import models
# Register your models here.


@admin.register(models.Comment)
class MessageAdmin(admin.ModelAdmin):
    fields = ["user", "room", "body"]
    list_display = ["user", "room", "body", "updated", "created"]


class TabularMessageAdmin(TabularInline):
    model = models.Comment
    fields = ["user", "room", "body"]
    extra = 0


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    fields = ["topic", "host", "title", "description", "participants", "image"]
    list_display = ["title", "topic", "host",
                    "description", "updated", "created"]
    list_per_page = 10
    inlines = [TabularMessageAdmin]


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ["title"]
    list_display = ["title"]
