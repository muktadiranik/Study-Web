from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("room/<str:pk>/", views.RoomDetail.as_view(), name="room"),
    path("create-room/", views.CreateRoom.as_view(), name="create-room"),
    path("update-room/<str:pk>/", views.UpdateRoom.as_view(), name="update-room"),
    path("delete-room/<str:pk>/", views.DeleteRoom.as_view(), name="delete-room"),
    path("delete-comment/<str:pk>/",
         views.DeleteComment.as_view(), name="delete-comment"),
    path("user-profile/<str:pk>/", views.UserProfile.as_view(), name="user-profile"),
    path("create-topic/", views.CreateTopic.as_view(), name="create-topic")
]
