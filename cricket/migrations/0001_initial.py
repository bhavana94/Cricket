# Generated by Django 2.2 on 2020-06-13 12:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.URLField(blank=True, max_length=4096, null=True, verbose_name='Player Image')),
                ('jersey_number', models.PositiveIntegerField(unique=True)),
                ('origin_country', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Player',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('logo', models.URLField(max_length=4096, verbose_name='Team Logo')),
                ('club_state', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Team',
                'ordering': ['team_name'],
            },
        ),
        migrations.CreateModel(
            name='PlayerMatchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('no_of_matches', models.PositiveIntegerField(blank=True, null=True)),
                ('highest_score', models.PositiveIntegerField(blank=True, null=True, verbose_name='Highest Score')),
                ('total_runs', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Runs')),
                ('total_wickets', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Wickets')),
                ('total_centuries', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Centuries')),
                ('total_fifties', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total Fifties')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player', to='cricket.Player', verbose_name='TeamPlayers')),
            ],
            options={
                'verbose_name': 'PlayerMatchData',
                'ordering': ['no_of_matches'],
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='players_team', to='cricket.Team', verbose_name='Team'),
        ),
        migrations.CreateModel(
            name='MatchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='away_team', to='cricket.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='cricket.Team')),
                ('winner_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='winners', to='cricket.Team')),
            ],
            options={
                'verbose_name': 'MatchData',
            },
        ),
    ]
