# Generated by Django 4.2 on 2023-05-15 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0008_alter_ingredientsspecific_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaderboardID', to='inventory.user_info')),
            ],
        ),
    ]
