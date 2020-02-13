# Setting Up Database on AWS 



# 

**In order to use MySQL instead of using SQLite, we can use RDS service provided by AMAZON WEB SERVICES**



AWS maintains server centres across different regions in the world. The closer to the server centres from our area gives faster response speed. Therefore, the region has to be set as the closest region from the area we live in. 



Regions you could use your AWS services will be as below. 



US East - 1

US East - 2

US West - 1 

US West - 2 



ASIA PACIFIC (HONG KONG) 

ASIA PACIFIC (MUMBAI)

ASIA PACIFIC (SEOUL)

ASIA PACIFIC (SINGAPORE)

ASIA PACIFIC (SYDNEY)

ASIA PACIFIC(TOKYO) 



CA - CENTRAL (CANADA)



EUROPE (FRANKFRUIT)

EUROPE (IRELAND)

EUROPE(LONDON)

EUROPE(PARIS)

EUROPE(STOCKHOLM)



MIDDLE EAST (BAHRAIN)



SOUTH AMERICA (BRAZIL )





# 1. Set the region 



For this project, I will be setting the region as ASIA PACIFIC (SEOUL)





# 2. Move to RDS 



Click RDS in the menu to move to RDS page. 





# 3. Create RDS parameter group 



RDS is a Relational Database services provided by AWS. Each virtual servers is referred as an instance. To use a MySQL, an instance has to be created. 



**A Parameter Group is a preset MySQL option** 



Parameter group has to be created to allow support Korean language. 



# 4. Create Parameter group 

#  

> Click on create Parameter Group 



- Set the parameter group family as [mysql5.7]
- Set the group name as onlineshop 
- Click on create to create a parameter 



# 5. Set up the options in Parameter Group



Search for Character in Parameter Filtering Search Bar 



Set the values as 'utf-8' except for the names contain numeric values for their allowed values. 





# 6. Create RDS instance 



The parameter group created will be applied to a RDS instance. 



Click on Instance menu on left. 



- Click on Create DATABASE

- Click on Engine type as MySQL 

- Click on MySQL 5.7.xx version as for the version. 

- Fill out fields in Settings (DB instance name, authority and passwords) 

- Set "YES" for public access possibilities. (The works will be added on local computer)

- Set up Database options 

  Database Name 

  DB Parameter Group (**Parameter Group [onlineshop] will be set here**) 

  Option Group 

- Set the backup frequency as 0. 





# Once a Parameter Group and RDS have been set, A security group need to be set up. 





**Set Up Security Group**



Once we check Security Group in the fields of Security and Network, We can check the security groups that the Database belongs to. 



**1) Inbound Security Group** 

​	Sets which IP range can be allowed to access to instance. Default setting will be that only my IP will 	be allowed to access to the instance. During the course of development practice, this value will be 	        set as all networks can access to instance. 

​	

​	click on Inbound Security Group. Edit it. 



Add 

Type : MYSQL/Aurora 

Protocol : TCP 

Port Range : 3306 

Source : 0:0:0:0 



**NB** When Deployed, this never be allowed. 





**2) Outbound Security Group** 





# Once an instance is created with appropriate settings, this database needs to be added to a project. 





