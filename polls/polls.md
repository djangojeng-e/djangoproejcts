Made another folder to start polls app guided in basic django tutorial on django's official website. 



# Write your first view



Go to polls/views.py and put the code in it. 



```python

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


```

The view has been created. Now, we might need to map it to a URL. 



**Create a file called urls.py in polls app folder.**



## Setting up polls/urls.py file 



polls.urls.py 



```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```



The root URLconf should be set as well. **go to mysite/urls.py,** add the following code. 

mysite/urls.py

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```



**include()** allows referencing other URLconfs. The main idea of include() is to make it easy to plug-and-play URLs. 



Polls are now in the own URLconf(polls/urls.py)



