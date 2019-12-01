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



## Time to Test so far 



$ python manage.py runserver 



Go to http://localhost:8000/polls/ in your browser. 

**polls/view.py contains the message "Hello, world. You're at the polls index."**  This should be displayed on this url. 



Make sure the directory paths are all correct. 

'> env'

'>mysite

​	/mysite 

   /polls 

​		manage.py '



# Database Setup 



Open **mysite/settings.py** 

By default, the configuration uses SQLite. 



At this point of time, there will be no need to use other databases than the default database which is SQLite3. Getting through this tutorial does not require to use the other database types. 



**Now, we need to create the tables in the database before we can use them.** 



$ python manage.py migrate 



The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file. 





# Creating Models 



**Define your models - your database layout, with additional metadata.** 



This is an important step to define your database. 



go to **polls/models.py** add the following code. 



```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

At this stage, it involves a bit of database concepts which does not come up to be familiar. A point to note here will be just the point below. 



**Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.** 



# Activating models



Firstly, we need to tell our project that the **polls app is installed.** 



------



> Django apps are 'pluggable' You can use an app in multiple projects, and you can distribute apps, because they don't have to be tied to a given Django installation. 

------



Go to **mysite/settings.py file and make polls app is installed in the** project. 



```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Now, Django knows to include polls app, run the command below. 



**$ python manage.py makemigrations polls** 



**makemigrations** tells Django that there had been some changes to the models. and store the changes as a migration. 

**migrate** is a command that will run the migrations for your and manage your database schema automatically. 



The tutorial induces to test SQL. 



$ python manage.py sqlmigrate polls 0001



**Tutorial explains about Database. This topic will be looked back later. The command sqlmigrate does not run the migration on your database.** 



## Run Migrate (This is hell important)





$ python manage.py migrate 



**migrate** command takes all the migrations that have not been applied and runs them against your database - synchronising the changes you made to your models with the schema in the database. 



**Advantages using Migrations** 



1. It is very powerful to let you change your models over time. 
2. You do not need to delete your database or tables and make new ones. 
3. Migrations specialises in upgrading your database live without losing data. 
4. As you do not need to directly change database in manipulating tables, it might save your time as you develop your project. 



#### Three-step guide to making model changes 



- Change your models (in models.py)
- Run $python manage.py makemigrations to create migrations for those changes. 
- Run $python manage.py migrate to apply those changes to the database. 



# Playing with the API





