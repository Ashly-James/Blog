from django.db import models


# enter templates on the settings
# install the app  on the installed app 'database name'
# import the models in the view
# goto the settings.py and change the database sections 
# Create your models here.
# class loginpge(models.Model):
# 	name=models.CharField(max_length=200)
# 	adres=models.CharField(max_length=300)		
# 	class Meta:
# 		db_table="logindemo"
		# after completing the model go to the command prompt and run the commands python manage.py makemigrations
		# 2. python manage.py migrate.Then we can see the 10+1 tables are created on our project database.
from django.contrib.auth.models import User
import os

class Registration(models.Model):
	fname=models.CharField(max_length=40)
	lname=models.CharField(max_length=20)
	emai=models.CharField(max_length=20)
	admin_status=models.CharField(max_length=20,default="Not Approved")
	blog=models.CharField(max_length=500,default="Null")
	class Meta:
		db_table="registratn"
class Blog(models.Model):
	emai=models.CharField(max_length=20)
	subjct=models.CharField(max_length=20,default="Null")
	blog=models.CharField(max_length=500)
	likes=models.CharField(max_length=500,default=0)

	class Meta:
		db_table="blog"
