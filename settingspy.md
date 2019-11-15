# This file lists out the contents in settings.py in the djnago projects


## BASE DIR[] 

  Root folders of Project Root folder, setting files or py file might be located  quite often. In order to faciliate this, this variable is set in advance. 

## SECRET KEY 

  Protection of session values or password changes urls can be worked out with
  this key. This key value should not be exposed. 

## DEBUG 

  Sets up the debug mode. if this is TRUE, error messages can be checked immedia  tely. In actual projects, it is set as FALSE. There is another setting value
  to make the adminisrator gets the error messages. 

## ALLOWED HOSTS  

  Setting up the hosts of Current service. Within development environment, this   is left empty. When the service is deployed or released, the value is set as 
  asterix. 

  It is recommended to use the actual domain to prevent DNS rebinding. 

  * From the release of Django 1.10.3 version, if DEBUG = FALSE and ALLOWED_HOSTS is empty, the service cannot be started. 


## INSTALLED APPS 

  Django web service consists of a combination of serveral apps. This lists out   the current apps in use.

##  MIDDLEWARE 

  Special frameworks used between all requests/responses messages. This normally  relates to security issues. 


## ROOT URLCON 

  F : identifies the file location of  urls.py. 


##  Templates 

  Settings to template systems used by Djnago. Template intepreter engine or change of template folder directory can be done. 

##  WSGI APPLICATION 

  Sets wsgi application. 

## DATABASES 

  Sets the DB 

## AUTH PASSWORD VALIDATOㄴ
  
  Used to verify the password. Basic Verification involves to validate with 
  user information, if it is numeric values, if it is too short or if it is too   common. 

## LANGUAGE CODE

  Django can implement multi language service easy. 

  

  
