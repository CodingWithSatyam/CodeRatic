from django.urls import path
from .views import Homeviews, templates
from .import views

urlpatterns = [
    path("", Homeviews.as_view(), name="index"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("templates/",templates.as_view(), name="templates"),
]
