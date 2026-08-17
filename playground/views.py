from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
# Create your views here.
# Take request -> return response
# request is an object that contains all the information about the request that was made to the server. It contains information such as the HTTP method (GET, POST, etc.), the URL, any query parameters, and any data that was sent with the request.
# request Handler is a function that takes a request object as an argument and returns a response object. The response object contains the data that will be sent back to the client, such as HTML, JSON, or an error message.
# In some framework its called action instead of view.

rooms = [
    {"id": 1, "name": "Room 1"},
    {"id": 2, "name": "Room 2"},
    {"id": 3, "name": "Room 3"},
]

def loginPage(request):
    context = {}
    return render(request,'playground/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "home.html", context)

def room(request, pk):
    # Find the room based on the primary key
    room = next((r for r in rooms if str(r["id"]) == pk), None)
    return render(request, "room.html", {"room": room})

def calculate():
    x = 10 + 10
    return x

def say_hello(request):
    # pull data from database
    # transform data
    # send email
    # return HttpResponse("Hello World")
    x = calculate()
    return render(request, "playground/hello.html", {'name': 'Django', 'result': x})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'playground/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request,'playground/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request,'playground/delete.html', {'obj': room})