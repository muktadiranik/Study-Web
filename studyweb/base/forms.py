from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Comment, Room, Topic
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["topic", "title", "description", "image"]

        widgets = {
            "topic": forms.Select(attrs={"class": "form-control", "placeholder": "Topic"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
            "description": forms.CharField(widget=CKEditorUploadingWidget()),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        labels = {
            "body": "",
        }
        widgets = {
            "body": RichTextFormField(config_name="default"),
        }
