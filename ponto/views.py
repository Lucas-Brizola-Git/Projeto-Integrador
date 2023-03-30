from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Pontos

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        return render(request, 'home.html')
    else:
        return redirect('/auth/login/?status=2')

#def registrar(request):
 #   if request.session.get('usuario'):
  #      try:
   #         ponto = Pontos(usuario = )
    #        ponto.save()
     #       return redirect('/auth/cadastro/?status=0')
      #  except:
       #     return redirect('/auth/cadastro/?status=4')
   # else:
    #    return redirect('/auth/login/?status=2')

def espelho(request):
    if request.session.get('usuario'):
        datein = "2023-01-01"
        datefin = "2023-04-20"
        usuario = Usuario.objects.get(id = request.session['usuario'])
        ponto = Pontos.objects.filter(usuario = usuario).filter(date__range=[datein, datefin])
        return render(request, 'espelho.html', {'pontos' : ponto})
    return redirect('/auth/login/?status=2')