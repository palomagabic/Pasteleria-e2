# Generated by Django 3.1.3 on 2020-12-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='desserts', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')),
            ],
            options={
                'verbose_name': 'dulce',
                'verbose_name_plural': 'Dulces',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='cake',
            options={'ordering': ['-updated', '-created'], 'verbose_name': 'torta', 'verbose_name_plural': 'tortas'},
        ),
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(upload_to='cakes', verbose_name='Imagen'),
        ),
    ]
