from atexit import register
from app.forms import *
from django import template
from app.models import *
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('app/tasks.html', takes_context=True)
def tasks_tag(context):
    context['tasks'] = Tasks.objects.all().order_by('complete', '-pk').filter(deleted=False, category__deleted=False)
    return context

@register.inclusion_tag('app/tasks.html', takes_context=True)
def deleted_tasks_tag(context):
    context['tasks'] = Tasks.objects.all().order_by('complete', '-pk').filter(Q(deleted=True) | Q(category__deleted=True))
    return context

@register.inclusion_tag('app/notes.html', takes_context=True)
def notes_tag(context):
    context['notes'] = Notes.objects.all().order_by('-pk').filter(deleted=False)
    return context

@register.inclusion_tag('app/notes.html', takes_context=True)
def deleted_notes_tag(context):
    context['notes'] = Notes.objects.all().order_by('-pk').filter(deleted=True)
    return context

@register.inclusion_tag('app/add_task.html', takes_context=True)
def add_task_tag(context, edit=False, task_id=None):
    context['form'] = NewTask()
    if edit == True:
        title = Tasks.objects.get(pk=task_id).title
        details = Tasks.objects.get(pk=task_id).details
        category = Tasks.objects.get(pk=task_id).category
        date = Tasks.objects.get(pk=task_id).date
        time = Tasks.objects.get(pk=task_id).time
        context['form'] = NewTask({
            'title': title,
            'details': details,
            'category': category,
            'date': date,
            'time': time
            })
    context['form_new_cat'] = NewCategory
    context['categories'] = CategoriesTasks.objects.all().filter(deleted = False)
    context['edit'] = edit
    return context

@register.inclusion_tag('app/add_note.html', takes_context=True)
def add_note_tag(context):
    context['form'] = NewNote
    return context

@register.inclusion_tag('app/login.html', takes_context=True)
def login_form_tag(context):
    context['form'] = LoginUser
    return context


@register.inclusion_tag('app/categories.html', takes_context=True)
def categories_tasks_tag(context):
    context['categories'] = CategoriesTasks.objects.all().filter(deleted=False)
    return context

@register.inclusion_tag('app/categories.html', takes_context=True)
def deleted_categories_tasks_tag(context):
    context['categories'] = CategoriesTasks.objects.all().filter(deleted=True)
    return context