# Generated by Django 4.2.9 on 2024-03-07 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=30)),
                ('contacto', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Enologos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telefono', models.IntegerField()),
                ('puesto', models.CharField(max_length=30)),
                ('tipo_contrato', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Id_Tanques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tanque', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MostoVino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variedad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tanques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tanque', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('variedad', models.CharField(max_length=40)),
                ('t', models.FloatField()),
                ('brix', models.FloatField()),
                ('ph', models.FloatField()),
                ('cliente', models.CharField(max_length=30)),
                ('enologo', models.CharField(max_length=30)),
                ('observaciones', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
