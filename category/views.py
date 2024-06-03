from django.shortcuts import render

# Create your views here.
def addCategory(request):
    return render(request, 'category.html')