from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Registration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerDisplay(request):
    return render(request, 'auth/registration/signup.html')

def handleSignup(request):
    if request.method == "POST":
        form_data = request.POST
        username = form_data['username']
        password = form_data['password']
        first_name = form_data['first_name']
        middle_name = form_data['middle_name']
        last_name = form_data['last_name']
        email = form_data['email']
        mobile = form_data['mobile']
        dob = form_data['dob']
        gender = form_data['gender']
        skills = form_data['skills']
        hobby = form_data['hobby']
        education_details = form_data['education_details']
        hashed_password = make_password(password)
        try:
            query = Registration.objects.create(username=username, password=hashed_password, first_name=first_name, middle_name=middle_name, last_name=last_name, email=email, mobile=mobile, dob=dob, gender=gender, skills=skills, hobby=hobby, education_details=education_details)
            query.save()
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('handleLogin')
        except Exception as e:
            messages.error(request, 'Something went wrong!')
    return render(request, 'auth/registration/signup.html')

def handleLogin(request):
    if request.method == "POST":
        loginuseremail = request.POST['email']
        loginpassword = request.POST['password']

        try:
            user = authenticate(request, username=User.objects.get(email=loginuseremail).username, password=loginpassword)
            registration_user = Registration.objects.get(email=loginuseremail)
            if user is not None and not user.is_staff:
                registration_user.last_login = timezone.now()
                registration_user.save()
                auth_login(request, user)
                messages.success(request, "Successfully logged In!")
                return redirect('dashboard', username=registration_user.username)
            elif user is not None and user.is_staff:
                auth_login(request, user)
                messages.success(request, "Successfully logged In!")
                return redirect("/admin")
            else:
                messages.error(request, 'Invalid credentials!')
                return render(request, 'auth/login.html')
        except (User.DoesNotExist, Registration.DoesNotExist):
            messages.error(request, 'Invalid credentials!')
            return render(request, 'auth/login.html')
    return render(request, 'auth/login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required(login_url='handleLogin')
def dashboard(request, username):
    if request.user.username != username:
        return redirect('handleLogin')
    else:
        try:
            loggedInUser = get_object_or_404(Registration, username=username)
            context = {
                'user_details': loggedInUser,  # Pass the user details to the template
            }
            return render(request, 'dashboard.html', context)
        except Exception as e:
            messages.error(request, "Something went wrong!")
            return redirect('handleLogin')