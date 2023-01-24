"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('enfermera/<int:id>', views.obtener_enfermera, 
            name='obtener_enfermera'),
        path('crear/enfermera', views.crear_enfermera, 
            name='crear_enfermera'),
        path('editar/enfermera/<int:id>', views.editar_enfermera, 
            name='editar_enfermera'),
        path('eliminar/enfermera/<int:id>', views.eliminar_enfermera, 
            name='eliminar_enfermera'),

        # patrones
        path('patron/<int:id>', views.obtener_patron, 
            name='obtener_patron'),
        path('crear/patron', views.crear_patron, 
            name='crear_patron'),
        path('editar/patron/<int:id>', views.editar_patron, 
            name='editar_patron'),
        path('crear/patron/enfermera/<int:id>', 
            views.crear_patron_enfermera, 
            name='crear_patron_enfermera'),

        # necesidades
        path('necesidad/<int:id>', views.obtener_necesidad, 
            name='obtener_necesidad'),
        path('crear/necesidades', views.crear_necesidad, 
            name='crear_necesidad'),
        path('editar/necesidad/<int:id>', views.editar_necesidad, 
            name='editar_necesidad'),
        path('crear/necesidad/enfermera/<int:id>', 
            views.crear_necesidad_enfermera, 
            name='crear_necesidad_enfermera'),

        # dominios
        path('dominio/<int:id>', views.obtener_dominio, 
            name='obtener_dominio'),
        path('crear/dominio', views.crear_dominio, 
            name='crear_dominio'),
        path('editar/dominio/<int:id>', views.editar_dominio, 
            name='editar_dominio'),
        path('crear/dominio/enfermera/<int:id>', 
            views.crear_dominio_enfermera, 
            name='crear_dominio_enfermera'),
 ]