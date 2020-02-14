# Create Media Server on AWS 



## The Reason to centralise the Database Server.



The reason as to why we centralise the Database server is to allow data being shared by several web server instances. Similarly, there are some files to share between different web servers. 



Media files and static files can be shared and used on S3. 



**S3 Settings**





S3 is used as per bucket units whereas Database and WebServers are used as per instances. 



In Order to use S3 as file storage, Django must install 2 modules.

 

- Install boto3 to use S3 services

- Install Django-storage to use variety of storage. 

  



```bash
pip install boto3 

pip install django-storages 
```





These Two modules will work together to allow the use of Amazon S3 services to use as a media server.**** 





**Go to config/settings.py to make appropriate settings.** 





```python
AWS_ACCESS_KEY_ID = 'IAM 엑세스 키 ID'
AWS_SECRET_ACCESS_KEY = "비밀 엑세스 키" 
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'django-onlineshop'
AWS_S3_CUSTOM_DOMAINS = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME_AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'

# ALL AWS VARIABLES are required variables for boto3


STATIC_URL = 'https://%s/%s' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFIELS_STORAGE = 'storages.backends.s3boto3.s3Boto3Storage'



```

Settings related to static files have been completed. Now, static files in the local storage need to be uploaded to S3. 



Collectstatic commands will allocate static files into one place. In this case, this will be on S3. 



```bash
python manage.py collectstatic 
```



