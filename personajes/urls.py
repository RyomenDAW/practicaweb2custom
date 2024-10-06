from django.urls import path
from . import views

urlpatterns = [
    path('personajes',views.personaje_list, name='personajes_list'),
    path('hechicero',views.hechicero_list, name='hechicero_list'),
    path('piromano',views.piromano_list, name='piromano_list'),
    path('marginado',views.marginado_list, name='marginado_list'),
    path('dexteridad',views.dexteridad_list, name='dexteridad_list'),

]
