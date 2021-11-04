from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import ortho_viewer.views
from django.views.decorators.csrf import csrf_exempt


def register(request):
    print("register button on")
    if request.method == "POST":
        print("register data get (POST)")
        
        if request.POST["password1"] == request.POST["password2"]:
            print("password correct")
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            print("register success")
        return redirect('login')
    return render(request, 'accounts/register.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
           return render(request, 'accounts/login.html', {'error': '아이디 혹은 비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
