# Generated by Django 5.0.2 on 2024-03-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_perro_imagen_alter_perro_fecha_desaparicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
