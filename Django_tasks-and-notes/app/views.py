from django.shortcuts import redirect, render
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import CategoriesTasks



def home(request):
    if request.POST:
        form_sel = request.POST.get('form_sel')
        if form_sel == 'add_task':
            form = NewTask(request.POST)
            if form.is_valid():
                form.save()
        elif form_sel == 'add_cat':
            form = NewCategory(request.POST)
            if form.is_valid():
                form.add_category(request.POST)
        elif form_sel == 'add_note':
            form = NewNote(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif form_sel == 'del_cat':
            cat = CategoriesTasks.objects.get(pk = request.POST.get('del_cat'))
            cat.deleted = True
            cat.save()
        elif form_sel == 'mark_task_complete':
            task = Tasks.objects.get(pk=request.POST.get('task_id'))
            task.complete = True
            task.save()
        elif form_sel == 'mark_task_uncomplete':
            task = Tasks.objects.get(pk=request.POST.get('task_id'))
            task.complete = False
            task.save()
        elif form_sel =='del_task':
            task = Tasks.objects.get(pk=request.POST.get('task_id'))
            task.deleted = True
            task.save()
        elif form_sel =='del_note':
            note = Notes.objects.get(pk=request.POST.get('note_id'))
            note.deleted = True
            note.save()
        elif form_sel == 'eidt_note':
            note = Notes.objects.get(pk=request.POST.get('note_id'))
            return redirect('/#add_note')
    return render(request, 'app/home.html')


def deleted(request):
    return render(request, 'app/deleted.html')



class register:
    form_class = UserCreationForm