# Generated by Django 3.0 on 2019-12-11 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agrodoce', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='negociacao',
            field=models.CharField(choices=[('avista', 'Pagamento á vista'), ('P2', 'Parcelado em 2x'), ('P3', 'Parcelado em 3x')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('Maquina', 'Maquina'), ('Legumes', 'Legumes'), ('Frutas', 'Frutas')], default=1, max_length=10),
        ),
    ]
