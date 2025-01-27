# Generated by Django 5.0.7 on 2024-08-04 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_login', models.DateTimeField(auto_now_add=True)),
                ('daily_entries', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boost_type', models.CharField(choices=[('speed', 'Speed Boost'), ('strength', 'Strength Boost'), ('spell amplification', 'Spell Amplification Boost'), ('spell resistence', 'Spell Resistence Boost'), ('precision', 'Precision Boost'), ('positive effect duration', 'Positive Effect Duration Boost'), ('attack speed', 'Attack Speed Boost'), ('cast time', 'Cast Time Boost')], max_length=30)),
                ('acquired_at', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boosts', to='player.player')),
            ],
        ),
    ]
