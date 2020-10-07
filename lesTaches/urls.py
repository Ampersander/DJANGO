"""
GestionTaches URL Configuration
"""
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('newTask',views.newTask,name="new_task"),
    path('viewTask/<name>',views.viewTask,name="view_task"),
    path('editTask/<name>',views.editTask,name="edit_task"),
    path('deleteTask/<name>',views.deleteTask,name="delete_task"),
    path('viewTask/<name>',views.viewTask,name="view_task"),
    path('list',views.task_listing,name="task_list"),
    path('newUser',views.newUser,name="new_user"),
    path('viewUser/<name>',views.viewUser,name="view_user"),
    path('editUser/<name>',views.editUser,name="edit_user"),
    path('deleteUser/<name>',views.deleteUser,name="delete_user"),
    path('listUser',views.user_listing,name="user_list"),

]
