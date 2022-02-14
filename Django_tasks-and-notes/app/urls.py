from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('del/', deleted, name='deleted'),
    path('register/', register, name='register')
]
