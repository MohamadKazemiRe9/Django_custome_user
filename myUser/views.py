from django.shortcuts import render , get_list_or_404,redirect
from .models import MyUser
from django.contrib.auth import authenticate , login ,logout
from .froms import RegisterForm , LoginForm , UpdateForm
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    users = get_list_or_404(MyUser)
    return render(request,'myUser/index.html',{"users":users,})

def register(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email = email,password = raw_password)
            login(request , user)
            return redirect("myUser:index")
        else:
            context['registerForm'] = form
    else:
        context['registerForm'] = RegisterForm()
    return render(request,'myUser/register.html',context)

def logout_view(request):
    logout(request)
    return redirect("myUser:index")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("myUser:index")
    context ={}
    user = request.user
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password = password)
            if user:
                login(request,user)
                return redirect("myUser:index")
            # else:
            #     context['loginForm'] = LoginForm()
            #     redirect("myUser:index")
    else:
        context['loginForm'] = LoginForm()
    
    context['loginForm'] = LoginForm()
    return render(request,'myUser/login.html',context)

def update_view(request):
    if not request.user.is_authenticated:
        return redirect("myUser:login")
    if request.POST:
        form = UpdateForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("myUser:index")
    else:
        form = UpdateForm(
            initial={
                'email' : request.user.email,
                'username' : request.user.username,
            }
        )
    return render(request,"myUser/update.html",{"updateForm":form})


