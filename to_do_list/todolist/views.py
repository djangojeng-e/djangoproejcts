from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.


def todoView(request):
    all_todo_items = TodoItem.objects.all()

    return render(request, 'todo.html', {'all_items': all_todo_items})

def addTodo(request):
    # create a new to do all_items
    # save
    # redirect the browser to

    new_item = TodoItem(content = request.POST['content'])
    new_item.save()

    return HttpResponseRedirect('/todo/')