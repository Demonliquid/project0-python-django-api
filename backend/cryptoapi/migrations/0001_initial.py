# Generated by Django 3.2.6 on 2021-08-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryptocurrency_name', models.CharField(max_length=100)),
                ('cryptocurrency_subtitle', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('market_cap', models.CharField(max_length=100)),
                ('change', models.CharField(max_length=100)),
            ],
        ),
    ]