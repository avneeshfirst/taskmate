from django.urls import path,include
from todo_app import views

urlpatterns = [
    path('', views.todo,name='todo'),
    path('delete/<task_id>', views.delete_task,name='delete_task'),
    path('edit/<task_id>', views.edit_task,name='edit_task'),
    path('complete/<task_id>', views.complete_task,name='complete_task'),
    path('markPending/<task_id>', views.markPending_task,name='markPending_task'),
    path('home', views.home,name='home'),
    
]
