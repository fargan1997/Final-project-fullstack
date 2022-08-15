from django.http.response import HttpResponse
from django.views.generic import TemplateView
from .models import Pelicula,Comentario
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render


class HomePageView(TemplateView):
    peliculas = Pelicula.objects.all()
    template_name="home.html"

    def get_context_data(self,*args,**kwargs):
        context = super(HomePageView,self).get_context_data(*args,**kwargs)
        context["peliculas"] = self.peliculas
        return context

class Perfil(TemplateView):
    template_name="perfil.html"


class Signup(TemplateView):
    template_name = "signup.html"
    # user correo contraseña
    def post(self,request):
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.firstname = name
        user.save()
        return HttpResponseRedirect(reverse('login'))
    


class Login(TemplateView):
    template_name="login.html"
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))     


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))     

class AdminPeliculas(TemplateView):
      template_name = "adminPeliculas.html"  

class ReproducionPelicula(TemplateView):
    template_name = "playPelicula.html"

    """def get(self, request, *args, **kwargs):
        print(kwargs)
        pelicula = list(Pelicula.objects.all().filter(id=1))[0]    
        return render(request,self.template_name,pelicula)"""
      
    def get_context_data(self,*args,**kwargs):
        context = super(ReproducionPelicula,self).get_context_data(*args,**kwargs)
        pelicula = list(Pelicula.objects.all().filter(id=kwargs['pk']))[0]    
        context["pelicula"] = pelicula
        return context   

class Comentarios(TemplateView):
    def get(self,request,*args,**kwargs):
        comentarios = list(Comentario.objects.all().filter(pelicula=kwargs['pk']))
        obj = ""
        arr = []
        for x in comentarios:
            obj = { 
                "nombre":x.usuario,
                "comentario":x.comentario
            }
            arr.append(obj)
            arr.append('$')
        arr.pop()
        #return HttpResponse({'comentario':comentarios,'usuario':comentarios.usuario})        
        return HttpResponse(arr)

    
    def post(self,request,*args,**kwargs):
        print("entro")
        _usuario = request.POST['id_usuario']
        _pelicula = list(Pelicula.objects.all().filter(id=kwargs['pk']))[0]#obtener una instancia de la pelicula
        _comentario = request.POST['comentario']
        comentario_usuario = Comentario(usuario=_usuario,pelicula=_pelicula,comentario=_comentario)
        comentario_usuario.save()
        return HttpResponse("ok")    