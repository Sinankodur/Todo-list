from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


from .forms import SignupForm, LoginForm
from .models import Task

def home(request):
    user = request.user
    if user.is_authenticated:
        tasks = Task.objects.filter(created_by=request.user)
    else:
        tasks = None
    return render(request, 'core/index.html', {'tasks': tasks})

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('/sign-in/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form' : form})

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))

    
    else:
        form = LoginForm()
    return render(request, 'core/signin.html', {'form' : form})

def sign_out(request):
    logout(request)
    return redirect('sign-in')

@login_required
def add_task(request):
    if request.method == 'POST':
        input_task = request.POST.get('task', '')
        task = Task.objects.create(name=input_task, created_by=request.user)

        return redirect('/')
    else:
        return redirect('/')
    
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'core/deleteConfirm.html', {'task': task})

def confirm_delete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')