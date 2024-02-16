from django.shortcuts import render
from django.urls import reverse
from django.views import View
from apps.users.forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, "blog/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "User seccesfuly registered")
            form.save()
            return redirect("blog:login-page")
        else:
            return render(request, "blog/register.html", {"form":form})

class UserLoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, "blog/login.html", {"form":form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
            messages.success(request, "user succesfully loged in")
            # 
            if user is not None:
                login(request, user)
                messages.success(request, "user succesfully loged in")
                return redirect(reverse("blog:user-profile", kwargs={"username":user.username}))       
            else:
                messages.warning(request, "User not found")
                return redirect("blog:login-page")
        else:
            return render(request, "blog/login.html", {"form":form})