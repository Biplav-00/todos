from typing import Any, Dict
from django.shortcuts import render,redirect
#from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import Task
#imported the newly created model called forms.py
from .forms import TaskForm,updateTaskForm,DisplayAllTaskForm
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin


# Create your views here.

class AddTask(FormMixin,ListView):
    model = Task
    form_class = TaskForm
    template_name= 'todo/add_task.html'
    context_object_name = 'task_data'
    
    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect('/')
        
 #This class is a generic classs and it has the limited or short code as compare to above class
class Index(ListView):
    model = Task
    # By default the index class return the object_list of model but we can set the naming convention manually
    context_object_name='task_data'
    
    #it render the model object in html template
    template_name = 'todo/index.html'      
    
    #override the base class method and passing the specific object with the helo of context
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        all_tasks = Task.objects.all().order_by('-date')
       # form = TaskForm()
        count_task=all_tasks.count()
        completed_todo = all_tasks.filter(complete=True).count()
        uncomplete_todo = count_task - completed_todo 
        context['all_tasks']=all_tasks
        context['count_task']=count_task
        context['completed_todo']=completed_todo
        context['uncomplete_todo']=uncomplete_todo
        #context['form']=form
        return context
    
    
            
class SingleView(DetailView):
    model = Task
    template_name = 'todo/single_view.html'
    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        form = DisplayAllTaskForm(instance=self.object)
        for field in form.fields:
            form.fields[field].disabled = True  
        context['form'] = form 
        return context 
     
     


#This class is used for updating task but the lines of  code is huge so we make it neat and clean with the help of below class just after this class
class Update(View):
    
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



class DeleteTodo(View):
    
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
        
    
    



