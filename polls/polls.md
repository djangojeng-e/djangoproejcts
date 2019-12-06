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



Django provides basic admin interface to allow staff or clients to add, change and delete content. 



Note : The admin is not intended to be used by site visitors. It's for the site managers. 



## Creating an admin user 



Create a user who can login to the admin site by running the command below. 



$ python manage.py createsuperuser 



The command will ask you to input username, email address and password. 

To test this admin page, enter the following command. 



$ python manage.py runserver 



Then, enter http://127.0.0.1:8000/admin/



#### Make the poll app modifiable in the admin 



Polls app is not displayed on the admin index page. We will need to tell the admin that Question objects have an admin interface. 



**Open polls/admin.py** and add the following codes. 



```python
from django.contrib import admin

from .models import Question

# Register your models here.


admin.site.register(Question)
```

Now, Django knows that Question has been registered and it should be displayed on the admin index page. 



Once you click on Questions, please note the followings. 



- The form is automatically generated from the Question model. 
- DateTimeField, CharField correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin. 
- DateTimeField gets free Javascript shortcuts. 



- Save - Saves changes and returns to the change-list page for this type of obejct. 
- Save and continue editing - Saves changes and reloads the admin page for this object. 
- Save and add another - Saves changes and loads a new, blank form for this type of obejct. 
- Delete - Displays a delete confirmation page. 



# Django Tutorial part 3. Views 





**Views** is a type of Web page in your Django application that generally serves a specific function and has a specific template. 



In polls applications, the following views will be implemented: 



- **Question "index" page** - displays the latest few questions. 
- **Question "detail" page** - displays a question text, with no results but with a form to vote. 
- **Question "results" page** - displays results for a particular question. 
- **Vote action** - handles voting for a particular choice in a particular question. 



**In Django, web pages and other contents are delivered by views.**





# Writing more views





**Few more views have to be added on polls/views.py**  These views are slightly different, because they take an argument. 



**Go to polls/views.py** 



```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```



New views have been added. Now, these new views should be wired into the polls.urls module by adding the following path() calls. 



**Go to polls/urls.py** and wire the new views into polls.urls.



```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



# Write views that actually do something



Since view is responsible for doing one of two things 

- Returning an HttpResponse object containing the content for the requested page 
- Raising an exception such as Http404. 



View can the followings: 

- Read records from a Database 
- Can use a template system such as Django's or third-party Python template system. 
- Generate a PDF file, output XML, create ZIP file on the fly
- Anything you want using whatever Python libraries you want. 



**A new index() view, which displays the latest 5 poll questions in the system, separated by commas, according to publication date.** 



```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```



Now, realise that the views.py has been hard-coded in the view. If you want to change the way the page looks, you will have to edit this Python code a lot. 



> There, Django's template system steps in to separate the design from Python by creating a template that the view can use!



**Now, create a directory called templates in polls directory**



**Templates** setting describes how Django will load and render templates.



> Django is unable to distinguish between the same template names. The right template must be pointed in Django. The easiest way to ensure this is by namespacing. 
>
> That is. putting those templates inside another directory named for the application itself. 



**Go to polls/templates/polls/index.html** 

This will be instructing Django what to display in the templates. 



```html

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}



```

**index view in polls/views.py has to be updated to use the template:**



Go to polls/views.py and update index(request) 



```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```



The code above loads the template called **polls/index.html** and passes it a context. The context is a dictionary mapping template variable names to Python objects. 



**There is a shortcut method : render()**

Find the polls/views.py using the shortcut. 



```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```



**The render() function takes the request object as its first argument, a template name as its second argument** and **a dictionary as its optional third** argument. It returns an **HttpResponse** object of the given template rendered with the given context. 





# Raising a 404 error 



Now, it is a time to tackle the question detail view - the page that displays the question text for a given poll. 



**Go to polls/views.py**



```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question 


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_quesiton_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id): # This part has been edited.
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id): 
    response = "You're looking at the results of quesiton %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): 
    return HttpResponse("You're voting on question %s." % question_id)

```



HTTP404 exception raised if a question with the request ID does not exist. 

polls/views.py has been udated with HTTP404 on detail. This should be applied to templates/polls/detail.html 

**Create a file polls/templates/polls/detail.html and add the following**



```html
{{ question }}
```



#### Using shortcuts detail() view, go to polls/views.py 



```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```



**get_object_or_404()** takes a Django model as its first argument and an arbitary number of keyword arguments, which it passes to the get() function of the model's manager. It raises Http404 if the object doesn't exist. 





# Use the template system



/templates/polls/detail.html has to be updated to give a look. 



```python
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

# Removing hardcoded URLs in templates 



Check out polls/index.html template 



Since polls.urls module defined the name argument in path() functions. **you can remove a reliance on specific URL paths defined in your url configurations by using the {% url %} template tag:** 



```django
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```



# Namespacing URL names 



In this tutorial, we only have polls app. However, in the real Django projects, there might be five, ten, twenty apps or more. 



Naming URLs could be issue as URL names should carry meanings of the URLs. URL names might have to indicate what the URL does or represent the app itself. What if there are same URL names in different apps? 



If one URL name is used in one app, the developer might want to use the same URL name for different apps too. 



**Keeping the namespaces of urls will come to be very important.**



Fortunately, Django provides the answer for this by adding namespaces to your URLconf. 



**To demonstrate this, go to polls/urls.py and add an app_name to set the application namespace:**



Go to **polls/urls.py and add app_name**



```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

Now, change templates/polls/index.html to point at the namespaced detail view. 



```django
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```





# Write a simple form





The tutorial updates poll detail template ("polls/detail.html") from the last tutorial. 



go to polls/templates/polls/detail.html

```django
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
<input type="submit" value="Vote">
</form>
```

**Quick notes here..** 



- Template displays a radio button for each question Choice. 

  The value of each radio button is the associated question Choice's Id. The name of each radio button is "Choice". 

- When the user selects one of the radio buttons and submits the form, it'll send the POST data choice=#. 

- action is set to {% url 'polls:vote' question.id %}

- method="post" is important because submitting this form will alter data server-side. 

- forloop.counter indicates how many times for tag has gone through the loop. 

- **{% csrf_token %} template tag protects Data from Cross Site Request Forgeries.** 



Go to polls/views.py, add the followings



```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

This code added does a few things that would sound very taunting to the beginners. At this stage, it might be wise to follow the process first here and come back to this point later. 



**Come back to polls/views.py, add the following to results()** 



```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

# 

polls/views.py points to polls/results.html. Hence, **the file has to be created. polls/templates/polls/results.html**. The, add the following codes. 



```django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```



# Use generic views: Less Code 



detail(), results(), index() views are similar. 

These views represent a common case of basic web development. 

**Getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template.** 



Django provides a shortcut, "generic views" system. Generic views abstract common patterns to the point where you don't even need to write Python code to write an app. 



Steps to make the use of generic views system. 



1. Convert the URLconf.
2. Delete some of the old, unneeded views. 
3. Introduce new views based on Django's generic views. 



### Amend URLconf



Go to polls/urls.py and amend it. 



```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



<question_id> has changed to <pk>



### Amend views 



Remove old index, detail, and results views and start using Django's generic views instead. To do so, 



Go to polls/views.py file and change it like below. 



```python
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```



**ListView and DetailView** are two generic views. These two views abstract the concepts of "display a list of objects" and "display a detail page for a particular type of obejct."





# Automated Testing 



Testing is a simple routine that check the operation of the code. 



Back in tutorial part2, we used the shell to examine the behaviour of a method, or running the application and entering data to check how it behaves. 



**Difference between automated tests and testing itself**



Automated tests is the testing work done for you by the system. You can check that your code still works as you originally intended, without having to perform time consuming manual testing. 



Without tests, the purpose or intended behaviour of an application might be rather opaque. 



> Jacob Kaplan-Moss, one of Django's original developers, says "Code without tests is broken by design"



Tests help team work together. Tests identify the areas to fix. Tests guarantee that colleagues don't inadvertently break your code and you don't break theirs without knowing. 



# Basic Testing Strategies 



### test-driven development 



Write the tests before writing the code. Describe a problem, then create some code to solve it. Test-driven development simply formalises the problem in a Python test Case. 



Doing the tests or writing some tests earlier is always right. 



Good testing practice is based on making a good choice on when to run the test. In many cases, it's good to write your first test the next time you make a change, either when you add a new feature or fix a bug. 





# Writing on first test  



### Identify a bug 



Question.was_published_recently() method returns True if the Question was published within the last day but also if the Question's pub_date field is in the future. 



Confirm the bug by using the shell to check the method on a question whose date lines in the future. 



$ python manage.py shell 



# Create a test to expose the bug





**Go to polls/tests.py and start writing the tests.** 



```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Here, django.test.TestCase subclass has been created with a method that creates a Question instance with a pub_date in the future. Then, check the output of was_published_recently() - ought to be False. 



# Running tests 



run the test using Terminal 



$ python manage.py test polls 



- manage.py test polls looked for tests in the polls application 
- found a subclass of django.test.Testcase class 
- Created a special database for the testing purpose 
- Looked for test methods - ones whose names begin with test
- test_was_published_recently_with_future_quesiton it created Question instance whose pub_date field is 30 days in the future 
- Using the assertIs() method, discovered that its was_published_recently() returns True, though we wanted it to return False. 



# Fixing the bug 



Go to polls.models.py 





```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

After a bug identified, we wrote a test that exposes it and corrected the bug in the code so our test passes. 



# More comprehensive test 



Further pin down the was_published_recently() method. 

Add two more test methods to the same class, to test the behaviour of the method more comprehensively: 



Go to polls/tests.py 



```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

Now we have three tests that confirms that Question.was_published_recently() returns sensible values for past, recent and future questions. 



# Test a View



The polls application is fairly undiscriminating: it will publish any question, including ones whose pub_date filed lies in the future. 

Improving this will involve setting a pub_date in the future. 



**A test for a view**



## The django Test Client 



Django provides a test Client to simulate a user interacting with the code at the view level. We can use it in tests.py or even in the shell. 



The tutorial demonstrates test using shell.  

Followed the instructions in the shell to see the results described in the tutorial. 



# Improving our view





go to polls/views.py and amend get_queryset() method 



# When testing, more is better 



Test codes are getting complicated. However, it is important to test. Once you write the code, you don't need to write them again. 



# Further Testing 





The tutorial only introduces some of the basic of testing. 



# Introduction to Static files



Web applications generally need to serve additional files - such as images, JavaScript, or CSS - necessary to render the complete web page. In Django, we refer to these files as "static files". 



**django.contrib.staticfiles** collects static files from each of your applications into a single location that can easily be served in production. 



# Customise your app's look and feel



create a folder static in polls directory. Django will refer to this folder for static files similar to the ways Django finds templates inside polls/templates. 



**Static file namespacing**



Just like templates, polls/static (rather than creating another polls subdirectory), but it would actually be a bad idea. 



Django will choose the first static file it finds whose name matches. Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. 



That is, by putting those static files inside another directory named for the application itself. 



**Create style.css in polls/static/polls/style.css**



add the following code 



```css
li a{
    color: green;
}
```



Next, add the following code at the top of **polls/templates/polls/index.html**



```django
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
```

**{% static %}** template tag generates the absolute URL of static files. 

That's all you need to do for development. 



# Adding a background-image



go to polls/static/polls/style.css 



add the following 



```css
body {
    background: white url("images/background.gif") no-repeat;
}
```



# Customise the admin form 





More than often, we all want to customise how the admin form looks and works. 



**go to polls/admin.py,** add the following 



```django
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```



# Adding related objects 



**go to polls/admin.py**



Register Choice with the admin just as we did with Question: 



```python
from django.contrib import admin

from .models import Choice, Question
# ...
admin.site.register(Choice)
```



Make it to add bunch of Choices directly when you create the Question object. Let's make that happen. 



Go to polls/admin.py. add the following codes. 



```python
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

Django offers a tabular way of displaying inline related objects. Change **ChoiceInline** declaration to read: 



go to polls/admin.py 



```python
class ChoiceInline(admin.TabularInline):
    #...
```



# Customise the admin change list



Django displays the **str()** of each object. It might be more helpful if we could display individual fields. To do that, use the **list_display** admin option which is a tuple of field names to display, as columns, on the change list page for the object: 



Go to polls/admin.py 



```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
```



You can improve further with a few attributes in **polls/models.py**



```python
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```

 

