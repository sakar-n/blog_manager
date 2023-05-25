from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("signup/", Registeruser.as_view(), name="signup"),
    path("", Homepage.as_view(), name="home"),
    path("login/", Loginpage.as_view(), name="login"),
    path("logout/", Logoutuser.as_view(), name="logout"),
    path("userblog/", Userblog.as_view(), name="userblog"),
    path("edit/<int:id>/", Editblog.as_view(), name="edit"),
    path("detail/<slug>", Blogdetail.as_view(), name="blogdetail"),
    path("delete/<int:id>/", Blogdelete.as_view(), name="delete"),
    path("create/",Createblog.as_view(),name="create"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='base/password_reset_form.html',html_email_template_name='base/reset_email.html'),name="reset_password"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'),name="reset_password_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'),name="reset_password_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'),name="password_reset_complete"),
]


