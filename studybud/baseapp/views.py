from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import User, Topic, Room, Message
from .form import RoomForm, UserCreationForm

# Create your views here.

def prof_logout(request):
    logout(request)
    return redirect('home')

def prof_login(request):
    correct = True
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            correct  = False
    context = {
        "correct": correct
    }
    return render(request, "login.html", context)

def signup(request):
    context = {

    }
    return render(request, "login.html", context)

def home(request):
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    messages = Message.objects.all()
    room_topic = rooms.filter(
        name__icontains = query
    )
    context ={
        "topics": topics,
        "room_topic":room_topic,
        "rooms": rooms,
        "messages": messages,
    }
    return render(request, "home.html", context)

def topics(request):
    query = request.GET.get("q") if request.GET.get("q") else ""
    topics = Topic.objects.filter(
        name__icontains = query
    )
    context = {
        "topics": topics
    }
    return render(request, "topics.html", context)

def profile(request, id):
    user = User.objects.all().get(id=id)
    topics = Topic.objects.all()
    messages = Message.objects.all()
    rooms = user.room_set.all()
    context = {
        "topics": topics,
        "messages": messages,
        "user": user,
        "rooms": rooms
    }
    return render(request, "profile.html", context)

def room(request, id):
    rooms = Room.objects.all().get(id=id)
    if request.method == "POST":
        message = request.POST.get("body")
        temp = Message.objects.create(
            host = request.user,
            room = rooms,
            messages = message
        )
        temp.save()
        rooms.participants.add(request.user)
        return redirect("room", id=id)
    participants = rooms.participants.all()
    context = {
        "rooms": rooms,
        "participants": participants
    }
    return render(request, "room.html", context)


def create_room(request):
    topics = Topic.objects.all()
    form = RoomForm()
    if request.method == "POST":
        topic, created = Topic.objects.get_or_create(name=request.POST.get("topics"))
        rooms = Room.objects.create(
            name = request.POST.get("name"),
            host = request.user,
            topic = topic
        )
        rooms.save()
        return redirect("home")

    context = {
        "form": form,
        "topics": topics,
    }
    return render(request, "create-room.html", context)
