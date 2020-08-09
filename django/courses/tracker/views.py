from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'course': Courses.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Courses.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/')

    Courses.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
    )
    return redirect('/')

def destroy(request, id):
  if request.method == "GET":
    context = {
        "course": Courses.objects.get(id=id)
    }
    return render(request,'destroy.html', context)

  if request.method == "POST":
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect("/")

def create(request):
    errors = Courses.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Courses.objects.create(
            name=request.POST['course_name']
        )
        desc = Description.objects.create(content=request.POST['desc'])
        course.description = desc
        course.save()

    return redirect("/")

def comments(request,id):
    context = {
        "course": Courses.objects.get(id=id)
    }
    return render(request,'comments.html', context)

def create_comment(request, id):
    errors = Comment.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Comment.objects.create(
            content=request.POST['content'],
            course = Courses.objects.get(id=id)
        )
    return redirect(f"/{id}")
