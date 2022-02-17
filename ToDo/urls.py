from django.urls import path
from .views import *

app_name = 'ToDo'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_read),
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete),
]