from django.urls import path, include

from aplicacion.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('acerca_de_mi', sobreMi, name='acerca_de_mi'),

    #______________________________ Busqueda (Perro)
    path('buscar_perros/', buscarPerros, name='buscar_perros'),
    path('encontrar_perros/', encontrarPerros, name='encontrar_perros'),

    #______________________________ Detalles (Perro)
    path('detalles_perro/<int:id>/', detallesPerro, name='detalles_perro'),

    #______________________________ Perros
    path('perros/', PerroList.as_view(), name='perros'),
    path('perro_create/', PerroCreate.as_view(), name='perro_create'),
    path('perro_delete/<int:pk>/', PerroDelete.as_view(), name='perro_delete'),
    path('perro_update/<int:pk>/', PerroUpdate.as_view(), name='perro_update'),

    #_______________________________ Detalles (Celulares)
    path('detalles_celular/<int:id>/', detallesCelular, name='detalle_celular'),

    #______________________________ Celulares
    path('celulares/', CelularList.as_view(), name='celulares'),
    path('celular_create/', CelularCreate.as_view(), name='celular_create'),
    path('celular_update/<int:pk>/', CelularUpdate.as_view(), name='celular_update'),
    path('celular_delete/<int:pk>/', CelularDelete.as_view(), name='celular_delete'),

    #_______________________________ Detalles (Zapatillas)
    path('detalles_zapatilla/<int:id>/', detallesZapatilla, name='detalles_zapatilla'),

    #______________________________ Zapatillas
    path('zapatillas/', ZapatillaList.as_view(), name='zapatillas'),
    path('zapatilla_create/', ZapatillaCreate.as_view(), name='zapatilla_create'),
    path('zapatilla_update/<int:pk>/', ZapatillaUpdate.as_view(), name='zapatilla_update'),
    path('zapatilla_delete/<int:pk>/', ZapatillaDelete.as_view(), name='zapatilla_delete'),

    #_______________________________ Detalles (Autos)
    path('detalles_auto/<int:id>/', detallesAuto, name='detalles_auto'),

    #______________________________ Autos
    path('autos/', AutoList.as_view(), name='autos'),
    path('auto_create/', AutoCreate.as_view(), name='auto_create'),
    path('auto_update/<int:pk>/', AutoUpdate.as_view(), name='auto_update'),
    path('auto_delete/<int:pk>/', AutoDelete.as_view(), name='auto_delete'),

    #______________________________ Login, Logout, Registrations
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('registrar/', register, name='registrar'),

    #______________________________ Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]