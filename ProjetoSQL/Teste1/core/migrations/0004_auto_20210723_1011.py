# Generated by Django 3.0 on 2021-07-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210723_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_curso', models.DecimalField(db_column='ID_CURSO', decimal_places=0, max_digits=18, primary_key=True, serialize=False)),
                ('nome_curso', models.CharField(db_column='NOME_CURSO', max_length=200)),
                ('data_cadastro', models.DateField(db_column='DATA_CADASTRO')),
                ('login_cadastro', models.CharField(db_column='LOGIN_CADASTRO', max_length=15)),
                ('data_alteracao', models.DateField(blank=True, db_column='DATA_ALTERACAO', null=True)),
                ('login_alteracao', models.CharField(blank=True, db_column='LOGIN_ALTERACAO', max_length=15, null=True)),
            ],
            options={
                'db_table': 'Cursos',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
