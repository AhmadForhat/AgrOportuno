# Generated by Django 3.0 on 2019-12-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('categoria', models.CharField(choices=[('Agricultor', 'Agricultor'), ('Lojista', 'Lojista')], max_length=10)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
    ]
