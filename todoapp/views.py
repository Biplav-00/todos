from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import Task
from django.template import context
#imported the newly created model called forms.py
from .forms import TaskForm,updateTaskForm

#these belows code are for the genreic views
from django.views import View


# Create your views here.

# def index(request):
#     #first fetch the all tasks(values) from db
#     all_tasks = Task.objects.all().order_by('-date')
#     count_task=all_tasks.count()
#     completed_todo = all_tasks.filter(complete=True).count()
#     uncomplete_todo = count_task - completed_todo  
#     if(request.method=='POST'):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form=TaskForm()  
#     context ={
#         'all_tasks': all_tasks,
#         'form':form,
#         'count_task':count_task,
#         'completed_todo':completed_todo,
#         'uncomplete_todo':uncomplete_todo,
#     }  
#     return render(request,'todo/index.html',context)
class index(View):
    
    def get(self,request):
        all_tasks = Task.objects.all().order_by('-date')
        form = TaskForm()
        count_task=all_tasks.count()
        completed_todo = all_tasks.filter(complete=True).count()
        uncomplete_todo = count_task - completed_todo 
        context={
            'all_tasks': all_tasks,
            'count_task':count_task,
            'completed_todo':completed_todo,
            'uncomplete_todo':uncomplete_todo,
            'form':form,
        }
        return render(request,'todo/index.html',context)

    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form=TaskForm()
        context={
            'form':form,
        }
        return render(request,'todo/index.html',context)
        


# def update(request,pk):
#     current_todo= Task.objects.get(id=pk)
#     if request.method=='POST':
#         form = updateTaskForm(request.POST,instance=current_todo)
#         if form.is_valid():
#             form.save()
#             return redirect ('/')
#     else:
#         form=updateTaskForm(instance=current_todo)
#     context={
#         'form' :form,
#     }
#     return render(request,'todo/update.html',context)


class update(View):
    
    def get(self,request,pk):
        current_todo= Task.objects.get(id=pk)
        form = updateTaskForm(instance=current_todo)
        context={
            'current_todo':current_todo,
            'form':form,
        }
        return render(request,'todo/update.html',context)
    
    def post(self,request,pk):
        current_todo= Task.objects.get(id=pk)
        form = updateTaskForm(request.POST,instance=current_todo)
        if form.is_valid():
            form.save()
            return redirect ('/')
    
        form=updateTaskForm(instance=current_todo)
        context={
            'form' :form,
            'current_todo':current_todo,
        }
        return render(request,'todo/update.html',context)


# def deleteTodo(request,pk):
#     selected_todo = Task.objects.get(pk=pk)
#     if request.method=='POST':
#         selected_todo.delete()
#         return redirect('/')
#     return render(request,'todo/delete.html')

class deleteTodo(View):
    
    def get(self,request,pk):
        selected_todo = Task.objects.get(pk=pk)
        context={
         'selected_todo':selected_todo
        }
        return render(request,'todo/delete.html',context)
     
    def post(self,request,pk):
        selected_todo = Task.objects.get(pk=pk)
        selected_todo.delete()
        return redirect('/')
        
    
    



