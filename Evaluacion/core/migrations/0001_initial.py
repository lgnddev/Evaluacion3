# Generated by Django 3.2.4 on 2021-06-16 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Categoria')),
                ('nombreCategoria', models.CharField(max_length=20, verbose_name='Nombre Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False, verbose_name='ISBN')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre Libro')),
                ('autor', models.CharField(max_length=30, verbose_name='Autor')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
