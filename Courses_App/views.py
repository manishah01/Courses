from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages

def index(request):
    return redirect(course)

def course(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request,'courses.html',context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        )
        messages.success(request, "Course successfully added")
        return redirect('/')
    
def confirm_delete(request,id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request,'confirm_delete.html',context)

def return_home(request):
    return redirect('/')

def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course successfully deleted")
    return redirect('/')


