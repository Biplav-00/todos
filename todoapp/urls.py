from django.urls import path
from . import views as view 

urlpatterns=[
  
    path("",view.index.as_view(),name="todo-index"),
    path('todo/', view.addTask.as_view() ,name='add_task'),
    path('todo/<int:pk>',view.singleView.as_view(),name='view'),
    path('todo/<int:pk>/update',view.update.as_view(),name="update"),
    path('todo/<int:pk>/delete',view.deleteTodo.as_view(),name='delete'),
    

   
]