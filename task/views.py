from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def addTask(request):
    if request.method == 'POST':
        form = forms.taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addTask')
    
    else:
        form = forms.taskForm()
    return render(request, 'addTask.html', {'form': form})

def edit_post(request, id):
    post = models.taskModel.objects.get(pk=id)
    form = forms.taskForm(instance=post)
    if request.method == 'POST':
        form = forms.taskForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('showAll')
    return render(request, 'addTask.html', {'form': form})

def delete_post(request, id):
    post = models.taskModel.objects.get(pk=id) 
    post.delete()
    # return redirect('addTask')
    return redirect('showAll')