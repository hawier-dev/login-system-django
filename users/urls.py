from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.sign_in, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
    path("logout/", views.logout, name="logout"),
]
