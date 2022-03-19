from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('edit_note/<int:note_id>/', edit_note, name='edit_note'),
    path('del/', deleted, name='deleted'),
    path('register/', register, name='register')
]
