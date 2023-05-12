from django.urls import path
from . import views as view 

urlpatterns=[
  
    path("",view.Index.as_view(),name="todo-index"),
    path('todo/', view.AddTask.as_view() ,name='add_task'),
    path('todo/<int:pk>',view.SingleView.as_view(),name='view'),
    path('todo/<int:pk>/update',view.Update.as_view(),name="update"),
    path('todo/<int:pk>/delete',view.DeleteTodo.as_view(),name='delete'),
    

   
]