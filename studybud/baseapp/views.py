from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import User, Topic, Room, Message
from .form import RoomForm, MyUserCreationForm, UserForm

# Create your views here.

def prof_logout(request):
    logout(request)
    return redirect('home')

def prof_login(request):
    page_status = "login"
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
        "correct": correct,
        "page_status": page_status,
    }

    return render(request, "login.html", context)

def signup(request):
    page_status = "signup"
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    print("testt", form)
    context = {
        "form": form,
        "page_status": page_status
    }
    return render(request, "login.html", context)

def settings(request):
    user = User.objects.get(id=request.user.id)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "settings.html", context)

def home(request):
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    topics = Topic.objects.all()[:7]
    rooms = Room.objects.all()
    messages = Message.objects.all()[:5]
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
    room_status = "default"
    context = {
        "rooms": rooms,
        "participants": participants,
        "room_status": room_status,
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
            topic = topic,
            description = request.POST.get("description")
        )
        rooms.save()
        return redirect("home")

    context = {
        "form": form,
        "topics": topics,
    }
    return render(request, "create-room.html", context)

def update_room(request, id):
    print("SDfasdfasdf TEST")
    topics = Topic.objects.all()
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == "POST":
        room_topic = request.POST.get("topics")
        topic, created = Topic.objects.all().get_or_create(name=room_topic)
        room.name = request.POST.get("name")
        room.topic = topic
        room.description = request.POST.get("description")
        room.save()
        return redirect("home")
    room_status = "edit"
    context = {
        "topics": topics,
        "form": form,
        "room_status": room_status,
    }
    return render(request, "create-room.html", context)

def remove_room(request, id):
    deletes = Room.objects.all().get(id=id)
    if request.method == "POST":
        deletes.delete()
        return redirect("home")
    feature = "room"
    context = {
        "deletes": deletes,
        "feature": feature,
    }
    return render(request, "delete.html", context)


def remove_message(request, id):
    deletes = Message.objects.all().get(id=id)
    if request.method == "POST":
        deletes.delete()
        return redirect("home")
    feature = "message"
    context = {
        "deletes":deletes,
        "feature": feature,
    }
    return render(request, "delete.html", context)