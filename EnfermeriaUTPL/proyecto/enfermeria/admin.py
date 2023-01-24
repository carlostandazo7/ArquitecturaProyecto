from django.contrib import admin

# Importar las clases del modelo
from enfermeria.models import Enfermera, Patron, Necesidad, Dominio

class EnfermeraAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Enfermera, EnfermeraAdmin)

class PatronAdmin(admin.ModelAdmin):

    list_display = ('nombrePatron', 'nroPatron')

    raw_id_fields = ('enfermera',)

admin.site.register(Patron, PatronAdmin)

class NecesidadAdmin(admin.ModelAdmin):

    list_display = ('nombreNecesidad', 'nroNecesidad')

    raw_id_fields = ('enfermera',)

admin.site.register(Necesidad, NecesidadAdmin)

class DominioAdmin(admin.ModelAdmin):

    list_display = ('nombreDominio', 'nroDominio')

    raw_id_fields = ('enfermera',)

admin.site.register(Dominio, DominioAdmin)