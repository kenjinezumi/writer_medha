from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('publications/', views.publication, name='publications'),
    path('editorial/', views.editorial, name='editorial'),
    path('prose/', views.prose, name='prose'),
    path('interviews/', views.interview, name='interviews'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]