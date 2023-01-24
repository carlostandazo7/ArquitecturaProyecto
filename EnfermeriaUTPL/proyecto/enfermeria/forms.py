from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from enfermeria.models import Enfermera, Patron, Necesidad, Dominio

class EnfermeraForm(ModelForm):
    class Meta:
        model = Enfermera
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese dirección por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }

class PatronForm(ModelForm):
    class Meta:
        model = Patron
        fields = ['nombrePatron', 'enfermera', 'nroPatron']

class PatronEnfermeraForm(ModelForm):

    def __init__(self, enfermera, *args, **kwargs):
        super(PatronEnfermeraForm, self).__init__(*args, **kwargs)
        self.initial['enfermera'] = enfermera
        self.fields["enfermera"].widget = forms.widgets.HiddenInput()
        print(enfermera)

    class Meta:
        model = Patron
        fields = ['nombrePatron', 'enfermera', 'nroPatron']


class NecesidadForm(ModelForm):
    class Meta:
        model = Necesidad
        fields = ['nombreNecesidad', 'enfermera', 'nroNecesidad']

class NecesidadEnfermeraForm(ModelForm):

    def __init__(self, enfermera, *args, **kwargs):
        super(NecesidadEnfermeraForm, self).__init__(*args, **kwargs)
        self.initial['enfermera'] = enfermera
        self.fields["enfermera"].widget = forms.widgets.HiddenInput()
        print(enfermera)

    class Meta:
        model = Necesidad
        fields = ['nombreNecesidad', 'enfermera', 'nroNecesidad']


class DominioForm(ModelForm):
    class Meta:
        model = Dominio
        fields = ['nombreDominio', 'enfermera', 'nroDominio']

class DominioEnfermeraForm(ModelForm):

    def __init__(self, enfermera, *args, **kwargs):
        super(DominioEnfermeraForm, self).__init__(*args, **kwargs)
        self.initial['enfermera'] = enfermera
        self.fields["enfermera"].widget = forms.widgets.HiddenInput()
        print(enfermera)

    class Meta:
        model = Dominio
        fields = ['nombreDominio', 'enfermera', 'nroDominio']