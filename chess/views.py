from .models import User
from django.http import *
from django.shortcuts import *
from django.core.mail import send_mail
import random

n=random.randint(1000,9999)
n=repr(n)
def home(request):
	return render(request,"chess/home.html")

def login (request):
	return render (request,"chess/login.html")

def signup(request):
	return render (request,"chess/signup.html")

def info_signup(request):
	user=User.objects.filter(username=request.POST['username'])
	if not user:
		username=request.POST['username']
		password=request.POST['password']
		email=request.POST['email']
		send_mail(
	    'Subject here',
	    'this is your activation code'+ n,
	    'icp95.project@gmail.com',
	    [email],
	    fail_silently=False,
		)

		user=User(username=username,email=email,password=password,activationcode= n )
		user.save()
		return render(request,"chess/info.html",{'user':user})
	else:
		error="user name already exist"
		return render(request,"chess/signup.html",{'error':error})

def info_login(request):
	users=user.objects.filter(username=request.POST['username'],password=request.POST['password'])
	if users:
		return render(request,"chess/info.html",{'user':users[0]})
			
	else:
	    error="try again"
	    return render(request,"chess.html",{'error':error})	
