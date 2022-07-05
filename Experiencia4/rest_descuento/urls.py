from django.urls import path
from rest_descuento.views import *
urlpatterns = [
    path('lista_descuento/',lista_descuento, name="lista_descuento"),
    path('detalle_descuento/<id>/',detalle_descuento,name="detalle_descuento"),
    path('lista_boleta/',lista_boleta, name="lista_boleta"),
    path('detalle_boleta/<id>/',detalle_boleta,name="detalle_boleta"),
    path('existe/', consulta_vigencia_sub, name="Existen_estos_suscriptors"),
    path('elimin/<id>',elim_sub,name='eliminar_suscriptor'),
    path('ing_sub/', ing_sub, name="Ingresar_usuario_y_suscriptor")
]