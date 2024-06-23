from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, PlantForm
from .models import Plant
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def upload(request):
    if request.method=='POST':
        form=(request.POST, request.FILES)
        print('I got here! Or something like that.')
        #if form.is_valid():
        plant=form.save()
        plant.owner=request.user.id
        print("I got here too!")
        plant.save()
        return HttpResponseRedirect('home')
    return render(request, 'upload.html', {})

def howtouse(request):
    return render(request, 'howtouse.html', {})

def login_user(request):
   if request.user.is_authenticated:
       return redirect('home')
  
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('home')
       else:
           # need an error message
           return redirect('login')
   else:
       return render(request, 'login.html', {})

def logout_user(request):
   logout(request)
   return redirect('home')

def register_user(request):
   if request.method == "POST":
       form = SignUpForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           return redirect('home')
      
   else:
       form = SignUpForm

   return render(request, 'register.html', {"form": form})

def dashboard(request):
    plants = Plant.objects.filter(user_id=request.user.id)
    print(plants)
    return render(request, "dashboard.html", {"request_method":request.method, "plants":plants})