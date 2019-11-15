
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

	9)  	
