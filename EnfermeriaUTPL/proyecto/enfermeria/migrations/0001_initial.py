# Generated by Django 4.1.5 on 2023-01-24 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('tipo', models.CharField(choices=[('patrones funcionales', 'Patrones Funcionales'), ('necesidades basicas', 'Necesidades Basicas'), ('dominios', 'Dominios')], max_length=25, verbose_name='Tipo de Patron')),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePatron', models.CharField(max_length=100, verbose_name='Nombre del Patron Funcional')),
                ('nroPatron', models.IntegerField(verbose_name='Numero del Patron Funcional')),
                ('enfermera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patrones', to='enfermeria.enfermera')),
            ],
        ),
        migrations.CreateModel(
            name='Necesidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreNecesidad', models.CharField(max_length=100, verbose_name='Nombre de la Necesidad Basica')),
                ('nroNecesidad', models.IntegerField(verbose_name='Numero de la Necesidad Basica')),
                ('enfermera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='necesidades', to='enfermeria.enfermera')),
            ],
        ),
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDominio', models.CharField(max_length=100, verbose_name='Nombre del Dominio')),
                ('nroDominio', models.IntegerField(verbose_name='Numero del Dominio')),
                ('enfermera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dominios', to='enfermeria.enfermera')),
            ],
        ),
    ]
