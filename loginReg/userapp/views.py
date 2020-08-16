from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return(render(request, 'index.html'))


def register(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect("/")
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        new_user = User.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], password=pw_hash)
        request.session['name'] = new_user.fname
        request.session['user_id'] = new_user.id
        request.session['function'] = "Registered"
        print(new_user.fname)
    return(render(request, 'success.html'))
    # return redirect('/')

def login(request):
    if request.method == 'POST':
        current_user = User.objects.filter(email=request.POST['email'])
        if len(current_user) > 0:
            current_user = current_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):
                request.session['name'] = current_user.fname
                request.session['user_id'] = current_user.id
                request.session['function'] = "Logged In"
            return(render(request, 'wall.html'))
    return redirect('/') 


# def success(request):
#     return(render(request, 'success.html'))

def logout(request):
    request.session.flush()
    return redirect('/')

def wall(request):
    context = {
        'all_messages' : Message.objects.all(), 'all_comments' : Comment.objects.all()
        }
    return (render(request,'wall.html', context))

def message(request):
    if request.method == "POST":
        errors = Message.objects.validator(request.POST)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/wall')
        post = Message.objects.create(content = request.POST['content'], owner = User.objects.get(id=request.session['user_id']))
        return redirect("/wall")
    redirect("/wall")

def comment(request, id):
    if request.method == "POST":
        errors = Comment.objects.validator(request.POST)
        if errors:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/wall')
        comment = Comment.objects.create(content = request.POST['content'], message = Message.objects.get(id=id), poster = User.objects.get(id=request.session['user_id']))
        return redirect("/wall")
    redirect("/wall")

def profile(request, id):
    context = {
        "one_user": User.objects.get(id=id)
    }
    return render(request,'profile.html', context)

def delete(request, id):
    Message.objects.get(id=id).delete()
    return redirect("/wall")