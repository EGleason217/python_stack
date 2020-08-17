from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


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
        new_user = User.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], password=pw_hash)
        request.session['name'] = new_user.fname
        request.session['user_id'] = new_user.id
    return(render(request, 'profile.html'))

def login(request):
    if request.method == 'POST':
        current_user = User.objects.filter(email=request.POST['email'])
        if len(current_user) > 0:
            current_user = current_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):
                request.session['name'] = current_user.fname
                request.session['user_id'] = current_user.id
                return(render(request, 'profile.html'))
            return redirect('/') 

def add(request):
    if request.method == 'POST':
        errors = Books.objects.validate(request.POST)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
                return redirect("/profile")
        new_book = Books.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploaded_by = User.objects.get(id=request.session['user_id']))
        return redirect('/profile')
    return redirect('/profile')

def profile(request):
    context = {
        'all_books' : Books.objects.all(),
    } 
    return render(request, "profile.html", context)

def book(request, id):
    context = {
        'current_book' : Books.objects.get(id=id),
        'current_user': User.objects.get(id=request.session['user_id']) 
    }
    return render(request,'book.html',context)

def delete(request, id):
    Books.objects.get(id=id).delete()
    return redirect("/profile")

def favorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Books.objects.get(id=book_id)
    user.favorited_books.add(book)

    return redirect(f'/book/{book_id}')

def unfavorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Books.objects.get(id=book_id)
    user.favorited_books.remove(book)

    return redirect(f'/book/{book_id}')

def update(request, book_id):
    book = Books.objects.get(id=book_id)
    book.desc = request.POST['description']
    book.save()
    return redirect(f'/books/{book_id}')