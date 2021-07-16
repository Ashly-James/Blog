from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Registration,Blog
from django.contrib.auth import login,authenticate,logout
from django.db.models import F
# Create your views here.\
def index_load(request):
	pass
	q1=Blog.objects.all()
	print("q1",q1)
	return render(request,"index.html",{"msg":q1})
def logout_view(request):
	logout(request)
	q1=Blog.objects.all()
	return render(request,"index.html",{"msg":q1})
def products(request):
	return render(request,"products.html")
	pass
def services(request):
	return render(request,"services.html")
def contact(request):
	return render(request,"contact.html")
def registration(request):
	return render(request,"registration.html")
def save_registration(request):
	# try:
	fnme=request.POST['txtfnme']
	lnme=request.POST['txtlnme']
	mail=request.POST['txtmail']
	pswd=request.POST['txtpswd']
	data1=Registration(fname=fnme,lname=lnme,emai=mail)
	data1.save()
	q=User.objects.create_user(username=mail,password=pswd,first_name=fnme,last_name=lnme)
	q.save
	q1=Blog.objects.all()
	print("q1",q1)
	return render(request,"index.html",{"msg":q1})

	# except Exception as e:
	# 	print(e) 					
def login(request):
	return render(request,"login.html")
def login_account(request):
	try:
		
		dict1={}
		passwrd=request.POST['txtpswd']
		usernme=request.POST['logmail']
		request.session['logmail']=usernme
		username=request.session['logmail']
		print("usernme",usernme)
		enter=Registration.objects.filter(emai=usernme,admin_status="Approved")
		print("qaa",enter)
		user1=authenticate(username=usernme,password=passwrd,is_superuser=1)
		print("user1",user1)
		if(user1.is_superuser):
			login(request)
			# return render(request,"admin_page.html")
			# count=Approved_users.objects.filter(admin_status="Approved").count()
			# job_count=Jobs.objects.count()
			# apply_job_count=Apply_job.objects.count()
			# aprvl=Approved_users.objects.filter(admin_status="Not Approved").count()
			# q=Approved_users.objects.filter(admin_status="Not Approved")
			q=Registration.objects.all()
			if q:
				return render(request,"admin_page.html",{"msg":q})

				# return render(request,"admin_page.html",{"msg":q,"msg1":count,"msg2":job_count,"msg3":apply_job_count,"msg4":aprvl})
			else:
				return render(request,"admin_page.html")
			# 	return render(request,"admin_index.html",{"msg":"No data"})
				# return redirect("admin123")
		elif enter:
			print("user login")
			username=request.session['logmail']
			user=authenticate(username=usernme,password=passwrd)
			if(user!=None):
				login(request)
				print("login success")
				
				q=Blog.objects.filter(emai=request.POST['logmail'])
				print("q",q)
				# qa=Jobs.objects.all()
				# dict1["q"]=qa
				
				# return render(request,"index.html",{"msg":q})
				return render(request,"user_personal_page.html",{"msg":q})
			
			else:

				return render(request,"login.html",{"msg":"Incorrect Username or password"})
		# elif(Approved_users.objects.filter(emai=usernme,admin_status="Rejected")):
			# return render(request,"login.html",{"msg":"Sorry admin reject your application"})
		elif(Registration.objects.filter(emai=usernme,admin_status="Not Approved")):

			return render(request,"login.html",{"msg":"Wait for the admin approval"})

	except Exception as e:
		print(e)
		# return render(request,"exception.html")
		return render(request,"login.html",{"msg":"Incorrect Username or passwordS"})
def admin_approval(request):
	idi=request.POST.get('id')
	print("id",idi)
	q=Registration.objects.all()
	if request.POST.get('id')!=None:

		Registration.objects.filter(id=idi).update(admin_status="Approved")
		return render(request,"admin_page.html",{"msg":q})
	elif request.POST.get("id1"):
		Registration.objects.filter(id=request.POST.get("id1")).update(admin_status="Rejected")
		return render(request,"admin_page.html",{"msg":q})
def blog_post(request):
	subject=request.POST['subject']
	blog=request.POST['blog']
	username=request.session['logmail']
	print("username",username)
	# data1=Registration()

	q=Registration.objects.filter(emai=username)
	q1=Blog.objects.all()
	if q:
		data1=Blog(emai=username,subjct=subject,blog=blog)
		data1.save()
	q1=Blog.objects.all()
	print("q1",q1)
	q2=Blog.objects.filter(emai=username)
	return render(request,"user_personal_page.html",{"msg":q2})
def user_edit_delete(request):
	pid=request.POST.get('edit_id')
	username=request.session['logmail']

	if request.POST.get('edit_id')!=None:
		# Blog.objects.filter(id=pid).update(blog=)
		q=Blog.objects.filter(id=pid,emai=username)
		return render(request,"user_blog_edit.html",{"msg":q})
	if request.POST.get('delete_id')!=None:
		pid=request.POST.get('delete_id')
		a=Blog.objects.get(id=pid)
		a.delete()
		q1=Blog.objects.filter(emai=username)
		print("q",q1)
		return render(request,"user_personal_page.html",{"msg":q1})

def blog_edit(request):
	pid=request.POST.get('id')
	username=request.session['logmail']
	q=Blog.objects.filter(emai=username)
	subject=request.POST['subject']
	# email2=request.POST['email1']
	# print(email2)
	update_blog=request.POST['blog']
	# q=Blog.objects.filter(id=pid,username=email)
	Blog.objects.filter(id=pid,emai=username).update(blog=update_blog,subjct=subject)
	return render(request,"user_personal_page.html",{"msg":q})

def admin_blog_view(request):
	q=Blog.objects.all()
	return render(request,"admin_blog_view.html",{"msg":q})
def admn_edit_delete(request):
	pid=request.POST.get('edit_id')
	print("sssssssssssssssss")
	username=request.session['logmail']
	q=Blog.objects.all()
	if request.POST.get('edit_id')!=None:
		# Blog.objects.filter(id=pid).update(blog=)
		q=Blog.objects.filter(id=pid,emai=username)
		print("q",q)
		# q=Blog.objects.filter(id=pid,emai=username)
		# return render(request,"user_blog_edit.html",{"msg":q})
		return render(request,"admin_edit_page.html",{"msg":q})
	elif request.POST.get('delete_id')!=None:
		pid=request.POST.get('delete_id')
		a=Blog.objects.get(id=pid)
		a.delete()
		q=Blog.objects.all()
		return render(request,"admin_blog_view.html",{"msg":q})
	elif request.POST.get('like_id')!=None:
		pid=request.POST['like_id']
		Blog.objects.filter(id=pid).update(likes=F('likes')+1)
		q=Blog.objects.all()
		return render(request,"admin_blog_view.html",{"msg":q})
	return render(request,"admin_blog_view.html",{"msg":q})
def admin_blog_edit(request):
	username=request.session['logmail']
	pid=request.POST.get('id')
	subject=request.POST['subject']
	update_blog=request.POST['blog']
	Blog.objects.filter(id=pid,emai=username).update(blog=update_blog,subjct=subject)
	q=Blog.objects.all()
	return render(request,"admin_blog_view.html",{"msg":q})
def usre_back(request):
	username=request.session['logmail']
	q=Blog.objects.filter(emai=username)
	return render(request,"user_personal_page.html",{"msg":q})
def like(request):
	pid=request.POST['id']
	return render(request,"like.html",{"msg":pid})
def like_add(request):
	pid=request.POST['id1']
	email=request.POST['email']
	if Registration.objects.filter(emai=email).exists():
		Blog.objects.filter(id=pid).update(likes=F('likes')+1)
		q=Blog.objects.all()
		return render(request,"index.html",{"msg":q})
	else:
		return render(request,"like.html",{"msg":"Please Register"})
		# return render(request,"index.html",{"msg":"ss"})
def admin_back(request):
	q=Registration.objects.all()
	return render(request,"admin_page.html",{"msg":q})