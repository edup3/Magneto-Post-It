# Generated by Django 5.0.1 on 2024-05-11 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0002_alter_vacante_imagen_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='colors',
            field=models.CharField(max_length=100, null=True),
        ),
    ]