from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import todo

# Create your views here.
def index(request):
    Todo = todo.objects.all()
    if(request.method == 'POST'):
        new_todo = todo(task = request.POST['task'])
        new_todo.save()
        return redirect('/')
    return render(request,'main_app/home.html',{'Todos':Todo})


def Delete(request,pk):
    Todo = todo.objects.get(id=pk)
    Todo.delete()
    return redirect('/')