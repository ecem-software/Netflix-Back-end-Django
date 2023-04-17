from django.urls import path
from user.views import *

urlpatterns=[
path("login",userLogin,name="login"),
path('register',register,name="register"),
path("create-profil",createProfil,name="create-profil"),
path("logout",oturumuKapat,name="logout"),
path("hesap",userProfil,name="hesap"),
path("delete",deleteUser,name="delete"),



]