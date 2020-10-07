from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task, User
from .forms import TaskForm, UserForm

# Create your views here.


def home(request):
    taches = Task.objects.all().order_by('-created_date')
    allTaches = len(taches)
    return render(request,'lesTaches/home.html', {"taches": taches.filter(closed=False), "total": allTaches })


def task_listing(request):
     objects = Task.objects.all().order_by('-created_date')
     return render(request,'lesTaches/list.html', {"taches": objects })

def viewTask(request, name):
    task = Task.objects.get(name = name)
    return render(request,'lesTaches/task.html',{"task":task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
        return render(request,'lesTaches/forms/task.html',{"form":form})


def editTask(request,name):
    task = Task.objects.get(name = name)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm(instance=task)
        return render(request,'lesTaches/forms/task.html',{"form":form})

def deleteTask(request, name):
    task = Task.objects.filter(name = name)
    task.delete()
    return HttpResponseRedirect(reverse('task_list'))


def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = UserForm()
        return render(request,'lesTaches/forms/task.html',{"form":form})

def user_listing(request):
     objects = User.objects.all().order_by('-name')
     return render(request,'lesTaches/listUser.html', {"users": objects })

def viewUser(request, name):
    user = User.objects.get(name = name)
    #tasks = Task.objects.all().filter(user = name)"tasks":tasks,
    return render(request,'lesTaches/user.html',{"user":user})

def editUser(request, name):
    user = User.objects.get(name = name)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        form = UserForm(instance=user)
        return render(request,'lesTaches/forms/user.html',{"form":form})

def deleteUser(request, name):
    user = User.objects.filter(name = name)
    user.delete()
    return HttpResponseRedirect(reverse('user_list'))
