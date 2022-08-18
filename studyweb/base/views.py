from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.views.generic import View
from django.db.models import Q, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from authenticate.models import User
from .models import Comment, Room, Topic
from .forms import CommentForm, RoomForm, TopicForm
# Create your views here.


class UserProfile(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        topics = Topic.objects.prefetch_related(
            "room_set").all().annotate(room_count=Count("room"))

        rooms = Room.objects.select_related(
            "host").filter(host_id=pk)
        comments = user.comment_set.all()

        current_room_count = rooms.count()
        return render(request, "base/profile.html", {
            "user": user,
            "rooms": list(rooms),
            "topics": list(topics),
            "current_room_count": current_room_count,
            "comments": comments,
        })


class Home(View):
    def get(self, request):
        try:
            user = User.objects.get(username=request.user)
        except:
            user = None
        topics = Topic.objects.prefetch_related(
            "room_set").all().annotate(room_count=Count("room")).order_by("title")

        q = request.GET.get("q")

        if q == None:
            rooms = Room.objects.select_related("host").all()
            comments = Comment.objects.select_related(
                "room").all().order_by("-updated")
        else:
            rooms = Room.objects.select_related(
                "host").filter(Q(topic__title__icontains=q) | Q(title__icontains=q))
            comments = Comment.objects.select_related(
                "room").filter(Q(room__topic__title__icontains=q)).order_by("-updated")

        current_room_count = rooms.count()

        return render(request, "base/home.html", {
            "rooms": list(rooms),
            "topics": list(topics),
            "current_room_count": current_room_count,
            "comments": comments,
            "user": user
        })


class RoomDetail(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        form = CommentForm

        comments = Comment.objects.select_related(
            "user").filter(room_id=room.id).order_by("-updated")
        participants = room.participants.all()

        return render(request, "base/room.html", {
            "room": room,
            "comments": comments,
            "form": form,
            "participants": participants
        })

    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        user = request.user

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.room = room
            comment.save()

            room.participants.add(request.user)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class DeleteComment(View):
    def get(self, request, pk):
        comment = Comment.objects.filter(pk=pk)
        comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CreateRoom(LoginRequiredMixin, View):
    login_url = "../authenticate/login"

    def get(self, request):
        return render(request, "base/room_form.html", {
            "form": RoomForm,
            "topic_form": TopicForm
        })

    def post(self, request):
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("home")


class CreateTopic(View):
    def post(self, request):
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            messages.success(request, "Topic added")
            return render(request, "base/room_form.html", {
                "form": RoomForm,
                "topic_form": TopicForm
            })


class UpdateRoom(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        form = RoomForm(instance=room)

        if request.user != room.host:
            messages.success(request, "No access")
            return redirect("home")

        return render(request, "base/room_form.html", {
            "room": room,
            "form": form,
            "update_flag": True
        })

    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect("home")


class DeleteRoom(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        if request.user != room.host:
            messages.success(request, "No access")
            return redirect("home")

        messages.success(request, "Deleted")
        return redirect("home")

    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return redirect("home")
