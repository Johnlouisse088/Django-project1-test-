from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),

    path("prof_logout/", views.prof_logout, name="logout"),
    path("prof_login/", views.prof_login, name="login"),
    path("signup/", views.signup, name="signup"),

    path("settings/", views.settings, name="settings"),

    path("topics/", views.topics, name="topics"),
    path("profile/<int:id>/", views.profile, name="profile"),
    path("room/<int:id>/", views.room, name="room"),

    path("create-room/", views.create_room, name="create_room"),
    path("update-room/<int:id>/", views.update_room, name="update_room"),
    path("remove-room/<int:id>/", views.remove_room, name="remove_room"),

    path("remove-message/<int:id>/", views.remove_message, name="remove_message"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)