from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import Task
from django.template import context
#imported the newly created model called forms.py
from .forms import TaskForm,updateTaskForm

#these belows code are for the genreic views
from django.views import View
from django.views.generic import ListView,UpdateView


# Create your views here.

#This function is responsible for initializing the index view

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

#this class is responsible for the rendering the index page with the help of View object and it has two method get and post 
# class index(View):
    
#     def get(self,request):
#         all_tasks = Task.objects.all().order_by('-date')
#         form = TaskForm()
#         count_task=all_tasks.count()
#         completed_todo = all_tasks.filter(complete=True).count()
#         uncomplete_todo = count_task - completed_todo 
#         context={
#             'all_tasks': all_tasks,
#             'count_task':count_task,
#             'completed_todo':completed_todo,
#             'uncomplete_todo':uncomplete_todo,
#             'form':form,
#         }
#         return render(request,'todo/index.html',context)

#     def post(self,request):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             form=TaskForm()
#         context={
#             'form':form,
#         }
#         return render(request,'todo/index.html',context)
        
 #This class is a generic classs and it has the limited or short code as compare to above class
 
class index(ListView):
    model = Task
    # By default the index class return the object_list of model but we can set the naming convention manually
    context_object_name='task_data'
    
    #it render the model object in html template
    template_name = 'todo/index.html'      
    
    #override the base class method and passing the specific object with the helo of context
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        all_tasks = Task.objects.all().order_by('-date')
        form = TaskForm()
        count_task=all_tasks.count()
        completed_todo = all_tasks.filter(complete=True).count()
        uncomplete_todo = count_task - completed_todo 
        context['all_tasks']=all_tasks
        context['count_task']=count_task
        context['completed_todo']=completed_todo
        context['uncomplete_todo']=uncomplete_todo
        context['form']=form
        return context
        

#this function is used to create the update view
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


#This class is used for updating task but the lines of  code is huge so we make it neat and clean with the help of below class just after this class

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
        
    
    



