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



The official Django tutorial on https://docs.djangoproject.com/en/2.2/intro/tutorial02/ lets us to experience the Free API django gives us. 



The tutorial wants to explain the Free API Django can provide through invoking the python shell. 



$ python manage.py shell 



By entering the command, you're entering in to the shell to explore database API. 



Tutorial goes through the below queries to create Question. This seems to access to the database directly. 



```python
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

q.question_text accesses to the class in models.py. **The value has been assigned as "what's up?"** 



However, this object is shown as **Question object(1)**. This is not a good representation of the object. Hence, **Question model in polls/models.py will be fixed to both Question and Choice.**





> **Make sure you exit python shell by pressing CTRL + D** 





Go to polls/models.py 

**Add str() method to both Question and Choice:** 



```python

from django.db import models

# Create your models here.

class Question(models.Model): 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): 
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



```



str() methods added to your models will give better representations used throughout Django's automatically-generated admin. 



**To add another custom method to this model, polls/models.py**



> Added import datetime, 
>
> Added from django.utils import timezone 
>
> and another function 
>
> def was_published_recently(self): 
>
> ​	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



```python


import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model): 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self): 
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


```

**import datetime** and **from django.utils import timzeone** have been added to reference Python's standard datetime module and Django's time-zone-related utilities in django.utils.timezone. 



**Now, we fixed our models to customise our representation of objects. Go back to python shell by command $python manage.py shell**



```python
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

Tutorial wants to test the modified models.py is working fine or not. At this stage, I realised that I need to study further on database queries etc. 



Playing with database API section finished with this testing. 





# Introducing the Django Admin





