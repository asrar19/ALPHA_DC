from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request : HttpRequest):
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
        new_user.save()
        #if register successful redirect to sign in page
        return redirect("users:sign_in")
    return render(request, "users/register.html")



def sign_in(request : HttpRequest):
    loggin_msg = None
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )
        if user is not None:
            #login user
            login(request, user)
            return redirect("alpha:index")
        else:
            loggin_msg = "Please Use correct Credentials"
    return render(request, "users/sign_in.html", {"msg" : loggin_msg})



def sign_out(request : HttpRequest):
    logout(request)
    return redirect("alpha:index")

