# Generated by Django 4.0.6 on 2022-08-10 04:28

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('celular_contacto', models.IntegerField()),
                ('correo_contacto', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_post', models.CharField(max_length=100)),
                ('subtitulo_post', models.CharField(max_length=100)),
                ('fecha_post', models.DateField()),
                ('contenido_post', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('estatus_post', models.BooleanField(blank=True, default=True)),
                ('imagen_post', models.ImageField(default='post_imagenes/default.png', null=True, upload_to='post_imagenes/')),
                ('usuario_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha_comentario', models.DateField()),
                ('estatus_comentario', models.BooleanField(blank=True, default=True)),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FECODER_APP.post')),
                ('usuario_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='avatars/default.png', upload_to='avatars', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
