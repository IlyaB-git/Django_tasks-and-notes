from re import L
from urllib import request
from .models import *
from django import forms


class NewTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['details'].required = False
        self.fields['category'].empty_label = None
    class Meta:
        model = Tasks
        fields = ['title', 'details', 'category', 'date', 'time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_in', 'placeholder': 'Задача'}),
            'details': forms.Textarea(attrs={'placeholder': 'Текст'})
        }
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'category_in'}),  queryset=CategoriesTasks.objects.filter(deleted=False))
    
    def edit_task(self, task_id):
        if self.is_valid():
            data = self.cleaned_data
            task = Tasks.objects.get(pk=task_id)
            task.title = data['title']
            task.details = data['details']
            task.category = data['category']
            task.date = data['date']
            task.time = data['time']
            task.save()



class NewCategory(forms.Form):
    new_category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'title_in', 'placeholder': ' Новая категория'}))
    cat_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    def add_category(self, post):
        model = CategoriesTasks()
        model.name = post.get('new_category')
        model.color = post.get('cat_color')
        model.save()

class NewNote(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['details'].required = False
        self.fields['image'].required = False
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    class Meta:
        model = Notes
        fields = ['title',  'details', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_in', 'placeholder': 'Заметка'}),
            'details': forms.Textarea(attrs={'placeholder': 'Текст'})
        }
    def edit_note(self, note_id, delete_img=None):
        if self.is_valid():
            data = self.cleaned_data
            note = Notes.objects.get(pk=note_id)
            note.title = data['title']
            note.details = data['details']
            note.color = data['color']
            if delete_img:
                note.image = None
            elif data['image']:
                note.image = data['image']
            note.save()

class LoginUser(forms.Form):
    login = forms.EmailField()
    pasword = forms.CharField()