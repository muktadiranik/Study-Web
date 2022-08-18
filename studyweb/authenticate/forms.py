from django import forms
from django.contrib.auth.forms import UserCreationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2", "image", "bio", "skills")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Lirst Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "type": "file"}),
            "skills": forms.SelectMultiple(attrs={"class": "form-control"}),
            "bio": forms.CharField(widget=CKEditorUploadingWidget())
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Type Password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Retype Password"
