from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'my_to_do_app/index.html')

def CreateTodo(request):
    user_input_str = request.POST['todoContent']
    return HttpResponse("Create todo를 할거야! =>" + user_input_str)

