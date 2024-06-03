from django.shortcuts import render

# Create your views here.
def taskAdd(request):
    return render(request, 'task.html')