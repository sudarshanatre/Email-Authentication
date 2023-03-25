from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
 



# Create your views here.
def home (request):
    return render(request , 'home.html')


def login_attempt(request):
    return render (request, 'login.html')


def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try: 

            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken .')
                return redirect('/register')

            
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User.objects.create(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()


            profile_object = Profile.objects.create(user = user_obj , auth_token = str(uuid.uuid4))
            profile_object.save()

            return redirect('/token')

        except Exception as a:
            print(a)




    return render (request, 'register.html')


def success(request):
    return render (request, 'success.html')


def token_send(request):
    return render (request, 'token_send.html')