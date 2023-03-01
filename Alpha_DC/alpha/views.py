from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Comment

# Create your views here.



############# THE INDEX PAGE ################

def index(request : HttpRequest):
    cookies = request.COOKIES
    return render(request, "alpha/index.html")




def consent_to_TOS(request : HttpRequest):
    response = redirect("alpha:index")
    response.set_cookie("consent", "Yes", max_age=60*60*24*7)

    return response




############# THE HOME PAGE ################

def home(request : HttpRequest):
    return render(request, "alpha/home.html")


#############  ABOUT PAGE ################

def about(request : HttpRequest):
    return render(request, "alpha/about.html")


#############  CONTACT PAGE ################

    
def contact(request : HttpRequest):
    
    if request.method == "POST":
        new_comment = Comment(user_name = request.POST["user_name"], user_comment = request.POST["user_comment"],subject = request.POST["subject"])
        new_comment.save()
        return redirect("alpha:thankyou" )
    return render(request, 'alpha/contact.html')



#############  THANK YOU MESSAGE PAGE FOR THE FEEDBACK IN CONTACT PAGE  ################


def thankyou(request : HttpRequest):
    return render(request, 'alpha/thankyou.html')



################################# SERVICES PAGE  THAT ASK THE USER TO ENTER INPUT #############################################


def services(request : HttpRequest):
    
    if request.method == "POST":
        nodes = request.POST["question1"]
        tier = request.POST["question2"]
        size = request.POST["question3"]
        sqft = int(request.POST["sqft"])
 
# main result 




############# MATH OPREATION FOR THE ( FIRST CHOICE  )  ################

        if nodes == "0-30" and tier == "1" and size == "small":
            buildingShelltotalLow = sqft * 80 
            buildingShelltotalHigh = sqft * 160

            electricalSystemltotalLow = sqft * 280
            electricalSystemtotalHigh = sqft * 460

            HVACtotalLow = sqft * 125 
            HVACtotalHigh = sqft * 215

            FiretotalLow = sqft * 15
            FiretotalHigh = sqft * 15

            FitOuttotalLow = sqft * 100
            FitOuttotalHigh = sqft * 200


            context = {
                "totalLow" : buildingShelltotalLow + electricalSystemltotalLow + HVACtotalLow + FiretotalLow +FitOuttotalLow ,
                "totalMax" : buildingShelltotalHigh + electricalSystemtotalHigh + HVACtotalHigh + FiretotalHigh + FitOuttotalHigh

                }
            return render(request, "alpha/services/service_1.html",context)




############# MATH OPREATION FOR THE ( SECOND CHOICE  )  ################


        elif nodes == "30-60" and tier == "2" and size == "medium":
            buildingShelltotalLow = sqft * 80 
            buildingShelltotalHigh = sqft * 160

            electricalSystemltotalLow = sqft * 280
            electricalSystemtotalHigh = sqft * 460

            HVACtotalLow = sqft * 125 
            HVACtotalHigh = sqft * 215

            FiretotalLow = sqft * 15
            FiretotalHigh = sqft * 15

            FitOuttotalLow = sqft * 100
            FitOuttotalHigh = sqft * 200


            context = {
                "totalLow" : buildingShelltotalLow + electricalSystemltotalLow + HVACtotalLow + FiretotalLow +FitOuttotalLow ,
                "totalMax" : buildingShelltotalHigh + electricalSystemtotalHigh + HVACtotalHigh + FiretotalHigh + FitOuttotalHigh

                }
            return render(request, "alpha/services/service_2.html",context)


############# MATH OPREATION FOR THE ( THIRD CHOICE  )  ################

        elif nodes == "60-90" and tier == "3" and size == "big" or "medium":
            buildingShelltotalLow = sqft * 80 
            buildingShelltotalHigh = sqft * 160

            electricalSystemltotalLow = sqft * 280
            electricalSystemtotalHigh = sqft * 460

            HVACtotalLow = sqft * 125 
            HVACtotalHigh = sqft * 215

            FiretotalLow = sqft * 15
            FiretotalHigh = sqft * 15

            FitOuttotalLow = sqft * 100
            FitOuttotalHigh = sqft * 200


            context = {
                "totalLow" : buildingShelltotalLow + electricalSystemltotalLow + HVACtotalLow + FiretotalLow +FitOuttotalLow ,
                "totalMax" : buildingShelltotalHigh + electricalSystemtotalHigh + HVACtotalHigh + FiretotalHigh + FitOuttotalHigh

                }
            return render(request, "alpha/services/service_3.html",context)
        


        ############# MATH OPREATION FOR THE ( 4TH CHOICE  )  ################


        elif nodes == "90-120" and tier == "4" and size == "big":
            buildingShelltotalLow = sqft * 80 
            buildingShelltotalHigh = sqft * 160

            electricalSystemltotalLow = sqft * 280
            electricalSystemtotalHigh = sqft * 460

            HVACtotalLow = sqft * 125 
            HVACtotalHigh = sqft * 215

            FiretotalLow = sqft * 15
            FiretotalHigh = sqft * 15

            FitOuttotalLow = sqft * 100
            FitOuttotalHigh = sqft * 200


            context = {
                "totalLow" : buildingShelltotalLow + electricalSystemltotalLow + HVACtotalLow + FiretotalLow +FitOuttotalLow ,
                "totalMax" : buildingShelltotalHigh + electricalSystemtotalHigh + HVACtotalHigh + FiretotalHigh + FitOuttotalHigh

                }
            return render(request, "alpha/services/service_4.html",context)



    return render(request, "alpha/services.html")




