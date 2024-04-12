from django.urls import path
from . import views
from .views import book_service

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.services, name='service'),
    path('price/', views.price, name='price'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('book_service/<int:service_id>/', views.book_service, name='book_service'),
    
    path('booked_services/', views.booked_services, name='booked_services'),
    path('delete_booked_service/<int:service_id>/', views.delete_booked_service, name='delete_booked_service'),
]


