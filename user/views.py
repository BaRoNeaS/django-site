from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, 'Başarıyla Kayıt Oldunuz.')
        return redirect("blog")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)
def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username ,password = password)
        if user is None:
            messages.error(request,"Kullanıcı Hadı Veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("blog")
    return render(request,"login.html",context)
def logoutuser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("blog")