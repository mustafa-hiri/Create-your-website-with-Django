from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('contact/', views.contact, name='contact'),
]
