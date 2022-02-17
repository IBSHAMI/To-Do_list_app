from django.contrib import admin
from .models import ToDo

# add ToDo to admin page
admin.site.register(ToDo)
