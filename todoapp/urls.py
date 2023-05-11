from django.urls import path
from . import views as view 

urlpatterns=[
    path("",view.index.as_view(),name="todo-index"),
    path('todo/<int:pk>/update',view.update.as_view(),name="todo-update"),
    path('todo/<int:pk>/delete',view.deleteTodo.as_view(),name='delete'),
   
]