# peliculas/urls.py
from django.urls import path
from .views import HomePageView,Perfil,Login,Logout,Signup,AdminPeliculas,ReproducionPelicula,Comentarios
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views  import  PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView




urlpatterns = [
    path("home",login_required(HomePageView.as_view()), name='home'),
    path("perfil",login_required(Perfil.as_view()), name="perfil"),
    path("singup",Signup.as_view(),name="singup"),
    path("accounts/login",Login.as_view(),name="login"),
    path("",Login.as_view()),
    path("adminPeliculas",AdminPeliculas.as_view(), name= "adminPeliculas"),
    path("pelicula/<int:pk>",ReproducionPelicula.as_view()),
    path("comentarios/<int:pk>",Comentarios.as_view()),

    path("accounts/password_reset/",PasswordResetView.as_view(), name="password_reset"),
    path("accounts/password_reset/done/",PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("accounts/reset/done/",PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    
    path("logout",Logout,name="logout")
]