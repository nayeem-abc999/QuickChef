# Generated by Django 4.2 on 2023-04-24 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_ingredientsspecific_dateofpurchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientsspecific',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]