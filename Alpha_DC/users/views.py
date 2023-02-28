


from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.db import IntegrityError


# Create your views here.


def register(request : HttpRequest):
    if request.method == "POST":
        new_user = User.objects.create_user(
            username=request.POST["username"], 
            email=request.POST["email"], 
            password=request.POST["password"], 
            first_name = request.POST["first_name"], 
            last_name = request.POST["last_name"]
            )
        
        new_user.save()
        #creating the profile
        user_profile = Profile(
            user=new_user, birth_date=request.POST["birth_date"], 
            gender=request.POST["gender"],
            company=request.POST["company"],
            job=request.POST["job"],
            creation_date=request.POST["creation_date"])   
        user_profile.save()
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

 

def profile_user(request : HttpRequest):
    user:User =request.user
    update_msg= None
    if request.method == "POST":
        try:
            user.username = request.POST.get('username',user.username) 
            user.first_name=request.POST["first_name"]
            user.last_name=request.POST.get("last_name",user.last_name)
            user.email=request.POST["email"]
        except IntegrityError:
            update_msg= "User exist"
        else:
            update_msg="update Succfully"
            user.save

        return render(request,"users:profile" , {"msg": update_msg})
    context = {"user":user , "msg":update_msg}
    return render(request, "users/register.html")








