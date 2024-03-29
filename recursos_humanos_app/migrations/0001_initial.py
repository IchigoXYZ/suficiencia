# Generated by Django 4.2.8 on 2024-02-14 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('carnet_identidad', models.CharField(max_length=20, unique=True)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos_humanos_app.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='TrabajadorDocente',
            fields=[
                ('trabajador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recursos_humanos_app.trabajador')),
                ('categoria_docente', models.CharField(choices=[('Instructor', 'Instructor'), ('Asistente', 'Asistente'), ('Auxiliar', 'Auxiliar'), ('Titular', 'Titular')], max_length=50)),
                ('categoria_cientifica', models.CharField(choices=[('Master', 'Máster'), ('Doctor', 'Doctor')], max_length=50)),
            ],
            bases=('recursos_humanos_app.trabajador',),
        ),
        migrations.CreateModel(
            name='TrabajadorNoDocente',
            fields=[
                ('trabajador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recursos_humanos_app.trabajador')),
                ('nivel_escolaridad', models.CharField(choices=[('9no', '9no grado'), ('Tecnico', 'Técnico Medio'), ('12mo', '12mo grado'), ('Universitario', 'Universitario')], max_length=20)),
                ('ocupacion', models.CharField(choices=[('Admin', 'Administrador'), ('TCI', 'TCI'), ('AuxServicios', 'Auxiliar de Servicios')], max_length=50)),
            ],
            bases=('recursos_humanos_app.trabajador',),
        ),
    ]
