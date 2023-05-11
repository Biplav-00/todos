from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    content = forms.CharField(label='Task Text Box',widget=forms.TextInput
                              (attrs={'placeholder':'Add task here'}))
    class Meta:
        model = Task
        fields = ['content']
        
        
class updateTaskForm(forms.ModelForm):
    content = forms.CharField(label='Update Task', widget=forms.TextInput(attrs={'placeholder':'Enter the text...'}))
    class Meta:
        model = Task
        fields =['content','complete']
        
    
    