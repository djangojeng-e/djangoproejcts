# djangoproejcts

contains simple djangoprojects

# Steps to create Django projects 

## 1. Create Virtual/Env project in pycharm 
## 2. Install Django using the command 

$ pip install django

* Terminal can be located on the bottom of Pycharm window.  

## 3. Create manage.py using the command
 
   $ django-admin startproject config .

## 4. Create DB file and initialise it using the command below. 

   $ python manage.py migrate 

## 5. Locate db.sqlite3 file after the command $ python manage.py migrate 


# After Step 5, there will be some exisitng files and folders in the project follder. 


 * config : Contains project setting file and required files for web service execution. This folder name has been named because of the command '$django-admin startproject'. However, the name of the folder does not have to be config folder. 
  

 * __init__.py : This is an empty file to make the project compatiable with python 2.x versions. It might not be necessary on Python 3.x. versions but the file keeps being created. 

 * setting.py : Contains variety of settings related to the projects. 

 * urls.py : One project may contain several url files. Each urls can be created to perform specific task(s). The settings and properties will be recorded in this file.

 * wsgi.py : This contains the content related to wsgi to operate web service. 

## Venv Folder

The folder contains the virtual environment. If possible, modificiations or deletions should be avoided. 

## db.sqlite3 

This is SQLite3 DB file. If SQLite DB is used, it should not be moved or deleted.

## manage.py 

The file is needed to execute variety of django commands. 


