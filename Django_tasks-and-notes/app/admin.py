from django.contrib import admin

from .models import *

admin.site.register(Notes)
admin.site.register(Tasks)
admin.site.register(CategoriesTasks)
