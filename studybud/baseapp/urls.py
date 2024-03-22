from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("prof_logout/", views.prof_logout, name="logout"),
    path("prof_login/", views.prof_login, name="login"),
    path("signup/", views.signup, name="signup"),

    path("topics/", views.topics, name="topics"),
    path("profile/<int:id>/", views.profile, name="profile"),
    path("room/<int:id>/", views.room, name="room"),
    path("create-room/", views.create_room, name="create_room"),
]