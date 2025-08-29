
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/<slug:slug>/", views.member_detail, name="member_detail"),
]
