# Generated by Django 4.0.dev20210701104232 on 2021-07-03 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(blank=True, max_length=15, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_presos')),
                ('telefone', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.telefone')),
            ],
        ),
    ]
