from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/", Registeruser.as_view(), name="signup"),
    path("", Homepage.as_view(), name="home"),
    path("login/", Loginpage.as_view(), name="login"),
    path("logout/", Logoutuser.as_view(), name="logout"),
    path("userblog/", Userblog.as_view(), name="userblog"),
    path("edit/<int:id>/", Editblog.as_view(), name="edit"),
    path("detail/<int:pk>/", Blogdetail.as_view(), name="blogdetail"),
    path("delete/<int:id>/", Blogdelete.as_view(), name="delete"),
  
]


