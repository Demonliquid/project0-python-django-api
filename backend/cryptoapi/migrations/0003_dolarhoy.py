# Generated by Django 3.2.6 on 2021-08-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapi', '0002_auto_20210823_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dolarhoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_dolar', models.CharField(max_length=100)),
                ('cotizacion_en_pesos', models.CharField(max_length=100)),
            ],
        ),
    ]
