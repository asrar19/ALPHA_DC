from django.urls import path
from . import views

app_name = "alpha"

urlpatterns = [
    path("", views.index, name="index"),
    path("consent/tos/", views.consent_to_TOS, name="consent_to_tos"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("thankyou/", views.thankyou, name="thankyou"),



]