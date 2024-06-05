from django.shortcuts import render
from task.models import taskModel
# Create your views here.
def showAll(request):
    info = taskModel.objects.all()
    # print(data)
    return render(request, 'show_all.html',{'data': info})