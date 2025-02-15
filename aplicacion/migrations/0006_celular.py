# Generated by Django 5.0.2 on 2024-03-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_rename_fecha_desaparicion_perro_fecha_de_desaparicion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('fecha_de_perdida', models.DateTimeField(help_text='Ingrese la fecha en el formato dd/mm/aaaa hh:mm')),
                ('lugar_de_perdida', models.CharField(max_length=100)),
            ],
        ),
    ]
