from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "Login successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # print('this is post method')
        # messages.error(request, "this is error message")

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists, please change!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists, please change!")
                    return redirect('register')
                else:
                    # all valid
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, "Register successfully and login")
                    return redirect('dashboard')
                    # user.save()
                    # messages.success(request, "Create account successfully")
                    # return redirect('login')
        else:
            messages.error(request, "Password do not match!")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')
