from django.urls import path
from .views import Homeviews
from .import views

urlpatterns = [
    path("", Homeviews.as_view(), name="index"),
    path("about/",views.about, name="about"),
]
