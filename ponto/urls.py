from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('espelho/', views.espelho, name = 'espelho'),
   # path('registrar/', views.registrar, name = 'registrar')  

]