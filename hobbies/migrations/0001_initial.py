# Generated by Django 3.1.7 on 2021-03-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='hobbies', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'Hobbies',
                'ordering': ['-created'],
            },
        ),
    ]