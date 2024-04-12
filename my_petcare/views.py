from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Service
from .models import BookedService
from django.urls import reverse
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'my_petcare/index.html')

def about(request):
    return render(request, 'my_petcare/about.html')

@login_required
def services(request):
    services = Service.objects.all()
    return render(request, 'my_petcare/service.html', {'services': services})

def price(request):
    return render(request, 'my_petcare/price.html')

def booking(request):
    return render(request, 'my_petcare/booking.html')

def contact(request):
    return render(request, 'my_petcare/contact.html')
    


#############User Authentication

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'my_petcare/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'my_petcare/register.html', {'form': form})
    
    
    
##################

from .forms import BookServiceForm

def book_service(request, service_id):
    
    service = Service.objects.get(pk=service_id)
    
    if request.method == 'POST':
        form = BookServiceForm(request.POST)
        if form.is_valid():
        
            booked_service = form.save(commit=False)
            booked_service.user = request.user 
            booked_service.service = service 
            booked_service.save()
            messages.success(request, 'Service booked successfully.')
            return redirect('home') 
    else:
        form = BookServiceForm()
    
    return render(request, 'my_petcare/book_service.html', {'form': form, 'service': service})

def booked_services(request):
    booked_services = BookedService.objects.filter(user=request.user)
    return render(request, 'my_petcare/booked_services.html', {'booked_services': booked_services})

@login_required
def delete_booked_service(request, service_id):
    
    booked_service = get_object_or_404(BookedService, pk=service_id)
    
    
    if request.user == booked_service.user:
        
        booked_service.delete()
        messages.success(request, 'Booked service deleted successfully.')
    else:
        
        messages.error(request, 'You are not authorized to delete this booked service.')
    
    return redirect('booked_services')