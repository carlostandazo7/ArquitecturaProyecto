from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from enfermeria.models import *

# importar los formularios de forms.py
from enfermeria.forms import *

def index(request):

    enfermeros = Enfermera.objects.all()

    informacion_template = {'enfermeros': enfermeros, 'numero_enfermeros': len(enfermeros)}
    return render(request, 'index.html', informacion_template)


def obtener_enfermera(request, id):

    enfermero = Enfermera.objects.get(pk=id)

    informacion_template = {'enfermero': enfermero}
    return render(request, 'obtener_enfermera.html', informacion_template)


def crear_enfermera(request):

    if request.method=='POST':
        formulario = EnfermeraForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EnfermeraForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_enfermera.html', diccionario)


def editar_enfermera(request, id):

    enfermera = Enfermera.objects.get(pk=id)
    if request.method=='POST':
        formulario = EnfermeraForm(request.POST, instance=enfermera)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EnfermeraForm(instance=enfermera)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_enfermera.html', diccionario)


def eliminar_enfermera(request, id):
    """
    """
    enfermera = Enfermera.objects.get(pk=id)
    enfermera.delete()
    return redirect(index)

# Crear patrones funcionales

def crear_patron(request):

    if request.method=='POST':
        formulario = PatronForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PatronForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_patron.html', diccionario)


def obtener_patron(request, id):

    enfermero = Enfermera.objects.get(pk=id)
    patron = Patron.objects.get(pk=id)

    informacion_template = {'enfermero': enfermero, 'patron': patron}
    return render(request, 'obtener_patron.html', informacion_template)


def editar_patron(request, id):

    patron = Patron.objects.get(pk=id)
    if request.method=='POST':
        formulario = PatronForm(request.POST, instance=patron)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PatronForm(instance=patron)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_patron.html', diccionario)


def crear_patron_enfermera(request, id):

    patron = Patron.objects.get(pk=id)
    if request.method=='POST':
        formulario = PatronEnfermeraForm(patron, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PatronEnfermeraForm(patron)
    diccionario = {'formulario': formulario, 'patron': patron}

    return render(request, 'crear_patron_enfermera.html', diccionario)

# Crear necesidades Basicas

def crear_necesidad(request):

    if request.method=='POST':
        formulario = NecesidadForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NecesidadForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_necesidad.html', diccionario)


def obtener_necesidad(request, id):

    enfermero = Enfermera.objects.get(pk=id)
    necesidad = Necesidad.objects.get(pk=id)

    informacion_template = {'enfermero': enfermero, 'necesidad': necesidad}
    return render(request, 'obtener_necesidad.html', informacion_template)


def editar_necesidad(request, id):

    necesidad = Necesidad.objects.get(pk=id)
    if request.method=='POST':
        formulario = NecesidadForm(request.POST, instance=necesidad)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NecesidadForm(instance=necesidad)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_necesidad.html', diccionario)


def crear_necesidad_enfermera(request, id):

    necesidad = Necesidad.objects.get(pk=id)
    if request.method=='POST':
        formulario = NecesidadEnfermeraForm(necesidad, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = NecesidadEnfermeraForm(necesidad)
    diccionario = {'formulario': formulario, 'necesidad': necesidad}

    return render(request, 'crear_necesidad_enfermera.html', diccionario)


# Crear Dominios

def crear_dominio(request):

    if request.method=='POST':
        formulario = DominioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DominioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_dominio.html', diccionario)


def obtener_dominio(request, id):

    enfermero = Enfermera.objects.get(pk=id)
    dominio = Dominio.objects.get(pk=id)

    informacion_template = {'enfermero': enfermero, 'dominio': dominio}
    return render(request, 'obtener_dominio.html', informacion_template)


def editar_dominio(request, id):

    dominio = Dominio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DominioForm(request.POST, instance=dominio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DominioForm(instance=dominio)
    diccionario = {'formulario': formulario}

    return render(request, 'crear_dominio.html', diccionario)


def crear_dominio_enfermera(request, id):

    dominio = Dominio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DominioEnfermeraForm(dominio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DominioEnfermeraForm(dominio)
    diccionario = {'formulario': formulario, 'dominio': dominio}

    return render(request, 'crear_dominio_enfermera.html', diccionario)
