

![Django REST Framework](https://www.django-rest-framework.org/img/logo.png)







> Django REST framework is a powerful and flexible toolkit for building Web APIs. 





Reasons to use REST framework 



- Web browsable API is a huge usability win for developers. 
- Authentication policies including packages for **OAuth1a** and **OAuth2**. 
- Serialization that supports both **ORM** and **non-ORM** data sources.
- Customizable **just use regular function-based views** if you don't need the more powerful features. 
- Extensive documentation 
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku and Eventtbrite. 









# Tutorial 1 : Serialization 





The tutorial will cover creating a simple pastebin code highlighting Web API. 





> Three packages to install 



```bash
pip install django 
pip install djangorestframework 
pip install pygments # This will be used for the code highlighting. 
```





.gitignore



```
/requirements.txt
/secrets.json

.idea
# Django User-uploaded static files root
/.media
/.static
app/*.ipynb

### Git ###
# Created by git for backups. To disable backups in Git:
# $ git config --global mergetool.keepBackup false
*.orig

# Created by git when using merge tools for conflicts
*.BACKUP.*
*.BASE.*
*.LOCAL.*
*.REMOTE.*
*_BACKUP_*.txt
*_BASE_*.txt
*_LOCAL_*.txt
*_REMOTE_*.txt

### Database ###
*.accdb
*.db
*.dbf
*.mdb
*.pdb
*.sqlite3

### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
db.sqlite3-journal
media

# If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/
# in your Git repository. Update and uncomment the following line accordingly.
# <django-project-name>/staticfiles/

### Django.Python Stack ###
# Byte-compiled / optimized / DLL files
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# Mr Developer
.mr.developer.cfg
.project
.pydevproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

### JupyterNotebooks ###
# gitignore template for Jupyter Notebooks
# website: http://jupyter.org/

.ipynb_checkpoints
*/.ipynb_checkpoints/*

# IPython
profile_default/
ipython_config.py

# Remove previous ipynb_checkpoints
#   git rm -r .ipynb_checkpoints/

### Linux ###
*~

# temporary files which can be created if a process still has a handle open of a deleted file
.fuse_hidden*

# KDE directory preferences
.directory

# Linux trash folder which might appear on any partition or disk
.Trash-*

# .nfs files are created when an open file is removed but is still being accessed
.nfs*

### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### PyCharm+all ###
# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio and WebStorm
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import
# When using Gradle or Maven with auto-import, you should exclude module files,
# since they will be recreated, and may cause churn.  Uncomment if using
# auto-import.
# .idea/modules.xml
# .idea/*.iml
# .idea/modules
# *.iml
# *.ipr

# CMake
cmake-build-*/

# Mongo Explorer plugin
.idea/**/mongoSettings.xml

# File-based project format
*.iws

# IntelliJ
out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Cursive Clojure plugin
.idea/replstate.xml

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based Rest Client
.idea/httpRequests

# Android studio 3.1+ serialized cache file
.idea/caches/build_file_checksums.ser

### PyCharm+all Patch ###
# Ignores the whole .idea folder and all .iml files
# See https://github.com/joeblau/gitignore.io/issues/186 and https://github.com/joeblau/gitignore.io/issues/360

.idea/

# Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-249601023

*.iml
modules.xml
.idea/misc.xml
*.ipr

# Sonarlint plugin
.idea/sonarlint

### Python ###
# Byte-compiled / optimized / DLL files

# C extensions

# Distribution / packaging

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.

# Installer logs

# Unit test / coverage reports

# Translations

# Scrapy stuff:

# Sphinx documentation

# PyBuilder

# pyenv

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.

# celery beat schedule file

# SageMath parsed files

# Spyder project settings

# Rope project settings

# Mr Developer

# mkdocs documentation

# mypy

# Pyre type checker

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

### VisualStudioCode Patch ###
# Ignore all local history of files
.history

### Windows ###
# Windows thumbnail cache files
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db

# Dump file
*.stackdump

# Folder config file
[Dd]esktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk



```





## Creating a model to work with 



The purpose of the tutorial is to start creating a simple Snippet model that is used to store code snippets. 



 

```python
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles 

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model): 
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    class Meta: 
        ordering = ['created']
        
```





# 1. Creating a Serializer class 



First thing to get started on the WEB API is to provide a way of serializing and deserializing the snippet instances into representations such as json. 



> Create a file snippets/serializer.py 





```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```



> The first part of the serializer class defines the fields that get serialized / deserialized. 



create() and update() methods define how fully fledged instances are created or modeified when calling serailizer.save() 



Serializer class is very similar to Django Form class. 



**The field flags can control how the serializer should be displayed in certain circumstances such as when rendering to HTML**



e.g. {'base_template': 'textarea.html'}



# Working with Serializers 



The tutorial creates a couple of code snippets to work with. 





```python
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

```



Now, a few snippet instances have been created. 

**The model instance has been translated into Python native datatypes.**



> To finalise the serialisation process, the data is rendered into json. 
>
> 

```python
serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}


content = JSONRenderer().render(serializer.data)
content
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'
```





Similarly, Deserialization is similar. parse a stream into Python native datatypes.. 





```python
import io 

stream = io.BytesIO(content)
data = JSONParser().parse(stream)



serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True 

serializer.validated_data
# OrderedDict 

serializer.save()
```



API is pretty similar to working with forms. The similarity should become even more apparent when writing views to use the serializer. 



We can also serialize querysets instead of model instances. we can simply add a many=True flag to the serializer arguments. 



```
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data 

```



# Using ModelSerializers



Similar to Django provides both form classes and ModelForm classes, REST framework includes both serializer classes and ModelSerializer classes. 



Refactoring serializer using the ModelSerializer class, replace the SnippetSerializer class with the following. 



```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet 
        fields = ['id', 'title', 'code', 'linenos','language', 'style']
```



**NB. ModelSerializer classes do not do anyting particular. They are simply a shortcut for creating serializer classes**



- An automatically determined set of fields. 
- Simple default implementations for the create() and update() methods. 





# Writing regular Django Views using Serializer





Create a regular django views. 



snippets/views.py 



```python
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer 

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

```





Created a snippet_list view listing out all code snippets. 

> We want to be able to POST to this view from lients that won't have a CSRF token we need to mark the view as csrf_exempt 
>
> This is not what we normally want to do but this will ensure meeting our purposes. 



We need a view which corresponds to an individual snippet, and can be used to retrieve, update or delete 





```python
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
```





snippets/urls.py 





```python
from django.urls import path 
from snippets import views 

urlpatterns = [
    path('snippets/', views.snippet_list), 
    path('snippets/<int:pk>', views.snippet_detail),
]


```



tutorial/urls.py to wire the root urlconf. 



```python
from django.urls import path, include 

urlpatterns = [ 
	path('', include('snippets.urls')),
]
```





> Note that there are couple of edge cases we're not dealing properly at the moment. 

If a request is made with a method that the view doesn't handle, it will end up with a 500 "server error" response. 





# Testing our first attempt at a Web API



Our API can be tested using curl or httpie. Httpie is a user friendly http client that's written in Python. 



To test the API, 



- get runserver 
- move to localhost/snippets/ 



```python
http http://127.0.0.1:8000/snippets/

HTTP/1.1 200 OK
...
[
  {
    "id": 1,
    "title": "",
    "code": "foo = \"bar\"\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  },
  {
    "id": 2,
    "title": "",
    "code": "print(\"hello, world\")\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  }
]

# We can get a particular snippet by referencing its id: 

http http://127.0.0.1:8000/snippets/2/

HTTP/1.1 200 OK
...
{
  "id": 2,
  "title": "",
  "code": "print(\"hello, world\")\n",
  "linenos": false,
  "language": "python",
  "style": "friendly"
}
```





> So far, Serialization API feels similar to Django's Forms API, and some regular Django Views. 

> 





# 2. Requests and Responses 



## Request objects 



REST framework introduces a request object that extends the regular HttpRequest, and provides more flexible request parsing. **request.data** is a core functionality of the Request object which is similar to request.POST. 



```python
request.POST 	# Only handles from data, Only works for 'POST' method 
request.data	# Handles arbitrary data. Works for 'POST', 'PUT' and 'PATCH' methods 
```





## Response objects 



REST framework also introduces a response object. which is a type of TemplateResponse that makes unrendered content and uses content negotiation to determine the correct content type to return to the client. 



```python
return Response(data)	# Renders to content type as requested by the client
```





## Status codes 



Numeric HTTP status codes in the views does not always make for obvious reading, it is not that easy to notice if you get an error code wrong. REST framework provides more explicit identifiers for each status code, such as HTTP_400_BAD_REQUEST in the status module. 



It's a good idea to use these throughout rather than using numeric identifiers. 



## Wrapping API views 



REST framework provides two wrappers you can use to wrie API views. 



- @api_view decorator for working with function based views. 
- APIView class for working with class-based views. 



These wrappers provide a few bits of functionality such as making sure you receive request instances in your view, and adding context to Response objects so that content negotiation can be performed. 



The wrappers also provide behaviour such as returning 405 Method Not Allowed responses which appropriate, and handling any ParseError exception that occurs when accessing request.data with malformed input. 





## Pulling it all together 





Fix the view with APIView, instead of JSONResponse, we use Response. 



Instance view is an imporvement over the previous view. It is a bit more concise and the code feels very similar to Forms API. Status codes are named with more meaningful words. 



The way it gets improved would feel very familiar. It shouldn't feel too much different from working with regular Django views. 



**request.data** can handle incoming json requests, but it can handle other formats. 



Similary, we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us. 







## Adding optional format suffixes to our URLs 



To take advantage of the fact that our responses are no longer hardwired to a single content type let's add support for format suffixes to our API endpoints. Using format suffixes gives URLs that explicity refer to a given format, and means the API will be able to handle URLs. 



```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns
```



Adding this will give a simple, clean way of referring to a specific format. 



## Testing the API 





```bash
# Enter the following command while the server is on runserver 

http http://127.0.0.1:8000/snippets/ 



HTTP/1.1 200 OK
...
[
  {
    "id": 1,
    "title": "",
    "code": "foo = \"bar\"\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  },
  {
    "id": 2,
    "title": "",
    "code": "print(\"hello, world\")\n",
    "linenos": false,
    "language": "python",
    "style": "friendly"
  }
]
```



> We can control the format of the response that we get back, either by using Accept header: 



```bash
http http://127.0.0.1:8000/snippets/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/snippets/ Accept:text/html         # Request HTML

http http://127.0.0.1:8000/snippets.json  # JSON suffix
http http://127.0.0.1:8000/snippets.api   # Browsable API suffix
```





> Similary, the format of the request that we send can be controlled using content-type header 





```bash
# POST using form data
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

{
  "id": 3,
  "title": "",
  "code": "print(123)",
  "linenos": false,
  "language": "python",
  "style": "friendly"
}

# POST using JSON
http --json POST http://127.0.0.1:8000/snippets/ code="print(456)"

{
    "id": 4,
    "title": "",
    "code": "print(456)",
    "linenos": false,
    "language": "python",
    "style": "friendly"}
    
    
 # Adding --debug switches to the http requests above, you will be able to see the request type in request headers. 
 
 
```





## Browsability 



API chooses the content type of the response based on the client request, it will by default return an HTML-formated representation of the resource when the resource is requested by a web browser. 



This allows for the API to return a fully web-browsable HTML representation. 



Having a web-browable API is a big win which makes developing and using the API much easier. It lowers the barrier-to-entry for other developers wanting to inspect and work with your API. 



