# Generated by Django 2.1.5 on 2021-06-27 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0004_comentarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentario',
        ),
    ]