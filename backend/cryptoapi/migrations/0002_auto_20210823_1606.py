# Generated by Django 3.2.6 on 2021-08-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrency',
            old_name='market_cap',
            new_name='market_number',
        ),
        migrations.AddField(
            model_name='cryptocurrency',
            name='market_unit',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]