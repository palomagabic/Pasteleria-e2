# Generated by Django 3.1.3 on 2020-12-09 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha edicion')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha publicacion')),
                ('image', models.ImageField(upload_to='receta', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha edicion')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('categories', models.ManyToManyField(related_name='get_post', to='receta.Category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-created'],
            },
        ),
    ]
