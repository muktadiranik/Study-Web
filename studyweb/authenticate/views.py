from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .forms import UserForm

# Create your views here.


class UpdateProfile(View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        form = UserForm(instance=user)
        return render(request, "authenticate/update_profile.html", {
            "user": user,
            "form": form,
            "update_flag": True
        })

    def post(self, request):
        user = User.objects.get(username=request.user)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            skills = form.cleaned_data["skills"]
            user = authenticate(request, username=username, password=password)
            user = User.objects.get(username=user)
            user.skills.clear()
            for i in skills:
                print(i)
                user.skills.add(i)

            login(request, user)

            messages.success(request, "Updated")
            return redirect("update-profile")
        else:
            messages.error(request, "Error")
            return render(request, "authenticate/update_profile.html", {
                "form": UserForm,
                "form": form,
                "update_flag": True
            })


class Register(View):
    def get(self, request):
        return render(request, "authenticate/register.html", {
            "form": UserForm,
        })

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            skills = form.cleaned_data["skills"]
            user = authenticate(request, username=username, password=password)
            user = User.objects.get(username=user)
            for i in skills:
                print(i)
                user.skills.add(i)

            login(request, user)

            messages.success(request, "Registered")
            return redirect("home")
        else:
            messages.error(request, "Error")
            return render(request, "authenticate/register.html", {
                "form": UserForm,
            })


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.success(request, "Already logged in")
            return redirect("home")
        return render(request, "authenticate/login.html", {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("home")
        else:
            messages.error(request, "User does not exists")
            return render(request, "authenticate/login.html", {})


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out")
        return redirect("home")
