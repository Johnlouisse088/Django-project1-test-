from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Topic, Room, Message

# Create your views here.

def home(request):
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    room_topic = rooms.filter(
        room__icontains = query
    )
    context ={
        "topics": topics,
        "room_topic":room_topic,
    }
    return render(request, "home.html", context)