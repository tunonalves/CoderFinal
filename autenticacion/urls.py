from django.urls import path
from . import views
from .views import VRegistro, cerrar_seccion, loguear


urlpatterns = [
    path('',VRegistro.as_view(), name="autenticacion"),
    path('cerrar_seccion',cerrar_seccion, name="cerrar_seccion"),
    path('loguear',loguear, name="loguear"),
]
