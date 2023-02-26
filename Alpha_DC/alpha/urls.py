from django.urls import path
from . import views

app_name = "alpha"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("vision/", views.vision, name="vision"),
    path("contact/", views.contact, name="contact"),


]