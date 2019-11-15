
Following commands should be input step by step. 




	1) $ python -m django --version (checks if django installed.) 

	2) $ django-admin startproject mysite (creates a project mysite.) 

	3) After 2), check if the following files and directories created. 
		mysite/ 
			manage.py 
			mysite/
				'__init__'.py
				settings.py
				urls.py
				wsgi.py


	4) Go to mysite/ directory and execute in command line. 
		
		$ python manage.py runserver 

	5) Check if the development server below is shown in terminal. 
	   
		http://127.0.0.1:8000/  


	6) Now, visit http://127.0.0.1:8000/ 
		if you see a message "Congratulations!" page with a rocket. 
		You are good to go ahead! 

	7) Let's create a new app. 
	   Make sure to create app in the same directory as manage.py 

		$ python manage.py startapp polls 

	8) Confirm if the following files and directories have been created 



			polls/
   			 __init__.py
    		         admin.py
   			 apps.py
    			 migrations/
        			__init__.py
    				models.py
    				tests.py
    				views.py



	9) Go to polls/url.py and add the following code. 


	from django.urls import path

	from . import views

	urlpatterns = [
    	path('', views.index, name='index'),
	] 


	10) Now, you will need to point the root URLconf at the polls.urls modeu	    le 

	go to mysite/urls.py, add the follwing code.  

	from django.contrib import admin
	from django.urls import include, path

	urlpatterns = [
    	path('polls/', include('polls.urls')),
    	path('admin/', admin.site.urls),
	]


	11) Verify if index view into the URLconf. 

		$ python manage.py runserver 

	go to http://localhost:8000/polls/

	N.B if you enter into http://localhost:8000/, you will get error. 



	# Setting UP Database


	1) Go to mysite/ open settings.py
	   Confirm the default contents. Run the following code in terminal. 
 

		$ python manage.py  	

	2) Edit polls/models.py 

		from django.db import models 

		class Questions(models.Model): 
		    question_text = 
		models.CharField(max_length=200)
		    pub_date = 
		models.DateTimeField('date published') 


		class Choice(models.Model): 
		    question = 
		models.ForeignKey(Question, 
		on_delete=models.CASCADE)
		    choice_text = 
		models.CharField(max_length=200)
		    votes = 
		models.IntegerField(Default=0)

	3) To include the app in the project, a reference to its configuration c	   lass has to be added in the INSTALLED_APPS setting. 

	   go to mysite/settings.py 

	   INSTALLED_APPS = [
    	   'polls.apps.PollsConfig',
    	   'django.contrib.admin',
    	   'django.contrib.auth',
    	   'django.contrib.contenttypes',
    	   'django.contrib.sessions',
    	   'django.contrib.messages',
    	   'django.contrib.staticfiles',
	   ]


	4) Now, polls app has been included in the project. Run another command: 

		$ python manage.py makemigrations polls 


	5) Once the following is shown on the output, 


	Migrations for 'polls':
  	polls/migrations/0001_initial.py:
    	- Create model Choice
    	- Create model Question
    	- Add field question to choice	


	6) run the command 

		$ python manage.py sqlmigrate polls 0001


	7) Run migrate again to create those model tables in the database. 


		$ python manage.py migrate 

	
