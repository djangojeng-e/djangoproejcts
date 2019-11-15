
# Execute the command 

python manage.py startapp app default



# After the command above, app default folder will be created and the following files will be created. 


## models.py 

  Model determines DB structure. In django, DB can be managed via models.py
  Models are made of class. Class names become table name, class properties become Column. 

  Regardless of DB type, models.py enables administrator or developer to manage   Relational DB. 


  Django employes ORM (Object Relational Mapping). 

  ORM lets the administrator or developer to create, search, edit and delete 
  data without having to know DB languages and API. 



## admin.py


  DB tables  can be created using model. This created tables need to be added,
  edited, deleted and searched. This is described as 

  ### CRUD (Create - Read - Update - Delete) 

  CRUD page needs to be created properly after Model is created properly. 

  Whenever created model needs to be checked in administration page or whenever
  the administrator or develop need to add special functionality, admin.py can 
  be edited to do so. 


## views.py 


  View consists of two type Class Based and Function Based. 
  Most of works involve creating view and editing it. 


## urls.py 

  Records the url to execute the view. 


# Templates 

  Usually contains HTML files. Normally exists in  template folder under the 
  app folders but it could also exist in project root. 

 
  


 
