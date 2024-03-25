from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Room, Topic, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RoomForm, UserForm, EditMessage
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm
from .models import CustomUser


def loginPage(request):
    page = 'login'

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!!')
            print("user do not exist!!")

        user = authenticate(username=email, password=password)

        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credential")
    context = {'page':page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')



def registerPage(request):
    page = 'register'
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, "An error occur, Please try again")
            
    return render(request, 'base/login_register.html', {'form':form})


def index(request):
    return render(request, 'base/index.html')


def home(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    
    topics = Topic.objects.all()[0:5]
    
    topicsHomes = Topic.objects.all()

    room_count = rooms.count()
    room_message = Message.objects.filter(Q(room__topic__name__icontains=q ))
    room_messages = Message.objects.all()[::-1]
    form = RoomForm()
    topic = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        
        topic, created = Topic.objects.get_or_create(name=topic_name)
     
        Room.objects.create(host=request.user, 
                            topic=topic, 
                            name=request.POST.get('name'), 
                            description=request.POST.get('description'))
        
        return redirect('home')
    context = {'form':form, 
               'topic':topic, 
               'topicHomes':topicsHomes,
               'rooms':rooms, 
               'topics':topics, 
               'room_count':room_count, 
               'room_message':room_message, 'room_messages':room_messages}
    return render(request, 'base/StudyLoungehome.html', context)


def activityPage(request):
    room_messages = Message.objects.all()[::-1]
    return render(request, 'base/activity.html', {'room_messages':room_messages})



def room(request, pk):
    room = Room.objects.get(id=pk)
    room_message = room.message_set.all()
    participants = room.participant.all()
  
    
    if request.method == "POST":
        message = Message.objects.create(
            user= request.user,
            room=room,
            body = request.POST.get('body')
        )
        room.participant.add(request.user)
        return redirect('room', pk=room.id)


  
 
    else:
        context = {'room':room, 'room_message':room_message, 'participants':participants, 'user':request.user, }
    return render(request, 'base/StudyLoungechatroom.html', context)




def edit_message(request, pk):
    message = get_object_or_404(Message, id=pk)
    
 
    if request.user != message.user:
        return HttpResponse("You are not allowed to edit this message.")
    
    if request.method == 'POST':
        form = EditMessage(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('room', pk=message.room.id)
        else:
            print("Error occurred")
    else:
        form = EditMessage(instance=message)
    
    return render(request, 'components/Room/update-message.html', {'edit_form': form, 'room_id': message.room.id})

def like_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    room = message.room
    user = request.user
    
    if user in message.likes.all():
        message.likes.remove(user)

    else:
        message.likes.add(user)

    return redirect('room', pk=room.id)



@login_required
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topic = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse("<h1 style='font-family:ABeeZee; position:fixed; left:23rem; top:10rem;'>How can i take to be of help to your life </h1>")

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('decription')
        room.save()
        return redirect('room', pk=room.id)
    context = {'form':form, 'topics':topic, 'room':room}
    return render(request, 'base/update-room.html', context)



@login_required
def user_profile(request, pk):
    user = CustomUser.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topicHomes = Topic.objects.all()
    topics = Topic.objects.all()[0:5]
    
    
    form = UserForm(instance=user)
    
    if request.method == "POST":
        form = UserForm(request.POST, instance=user )
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    context = {'user':user, 'rooms':rooms, 'topics':topics, 'room_message':room_message, 'topicsHomes':topicHomes, 'form':form}
    return render(request, 'base/profile.html', context)


@login_required
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
        
    return render(request, 'base/delete.html', {'room_obj':room})


@login_required
def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    room_id = message.room.id
    print('room id: ',room_id)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')
    message.delete()
    messages.success(request, "Message Deleted ")
    return redirect('room', pk=room_id)


    
        
        




def topics_page(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    topicHomes = Topic.objects.all()
    return render(request, 'base/topics.html',{'topics':topics, 'topicHomes':topicHomes})


