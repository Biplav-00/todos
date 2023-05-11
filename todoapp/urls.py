from django.urls import path
from . import views as view 

urlpatterns=[
    path("",view.index,name="todo-index"),
    path('update/<int:pk>/',view.update,name="todo-update"),
    path('delete/<int:pk>/',view.deleteTodo,name='delete'),
   
]