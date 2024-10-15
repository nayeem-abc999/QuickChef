# Generated by Django 4.2 on 2023-05-16 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_ingredientsspecific_quantity'),
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='id',
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='leaderboardID', serialize=False, to='inventory.user_info'),
        ),
    ]