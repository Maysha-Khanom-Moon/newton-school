from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        receipe_image = request.FILES['receipe_image']
        
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        
        return redirect('/receipes/') 

    queryset = Receipe.objects.all()
    result = "All Receipe"
    
    if search_receipe := request.GET.get('search_receipe'):
        # print(search_receipe)
        queryset = queryset.filter(receipe_name__icontains = search_receipe)
        result = "Searched Result"
    
    context = {'receipes': queryset, 'result': result}
    
    return render(request, 'home/index.html', context)


# to delete receipe
@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')


# to update receipe
@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        
        queryset.receipe_name = data.get('receipe_name')
        queryset.receipe_description = data.get('receipe_description')
        
        if 'receipe_image' in request.FILES:
            queryset.receipe_image = request.FILES['receipe_image']
    
        queryset.save()
        return redirect('/receipes/')
    
    context = {'receipe': queryset}
    
    return render(request, 'home/update_receipe.html', context)


# maysha412@gmail.com
# wiener
# 1234
# to login
def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if not User.objects.filter(username = username,).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        if not User.objects.filter(email = email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('/login/')
        
        user = authenticate(email = email, username = username, password = password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')
        
    
    return render(request, 'home/login.html')

# to register
def register_page(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        
        return redirect('/login/')
    
    return render(request, 'home/register.html')


# to logout
def logout_page(request):
    logout(request)
    return redirect('/login/')


def vege(request):
    return render(request, 'home/show.html')