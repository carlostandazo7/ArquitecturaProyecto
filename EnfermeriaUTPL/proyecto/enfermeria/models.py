from django.db import models

class Enfermera(models.Model):

	opcionesTipo = (
		('patrones funcionales', 'Patrones Funcionales'),
		('necesidades basicas', 'Necesidades Basicas'),
		('dominios', 'Dominios'),
	)
	nombre = models.CharField('Nombre', max_length=30)
	direccion = models.CharField('Direccion', max_length=30)
	ciudad = models.CharField('Ciudad', max_length=30)
	tipo = models.CharField('Tipo de Patron', max_length=25, choices=opcionesTipo)

	def __str__(self):
		return "%s %s %s %s" % (self.nombre,
			self.direccion,
			self.ciudad,
			self.tipo)

class Patron(models.Model):
    nombrePatron = models.CharField('Nombre del Patron Funcional' ,max_length=100)
    nroPatron = models.IntegerField('Numero del Patron Funcional')
    enfermera = models.ForeignKey(Enfermera, on_delete=models.CASCADE,
            related_name="patrones")

    def __str__(self):
        return "%s %d" % (self.nombrePatron,
        	nroPatron)

class Necesidad(models.Model):
    nombreNecesidad = models.CharField('Nombre de la Necesidad Basica' ,max_length=100)
    nroNecesidad = models.IntegerField('Numero de la Necesidad Basica')
    enfermera = models.ForeignKey(Enfermera, on_delete=models.CASCADE,
            related_name="necesidades")

    def __str__(self):
        return "%s %d" % (self.nombreNecesidad,
        	nroNecesidad)

class Dominio(models.Model):
    nombreDominio = models.CharField('Nombre del Dominio' ,max_length=100)
    nroDominio = models.IntegerField('Numero del Dominio')
    enfermera = models.ForeignKey(Enfermera, on_delete=models.CASCADE,
            related_name="dominios")

    def __str__(self):
        return "%s %d" % (self.nombreDominio,
        	nroDominio)
