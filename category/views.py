from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def addCategory(request):
    if request.method == 'POST':
        form = forms.categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addCategory')
    
    else:
        form = forms.categoryForm()
    return render(request, 'addCategory.html', {'form': form})