# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raceheat',
            name='ended_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Heat ended time'),
        ),
        migrations.AddField(
            model_name='raceheat',
            name='number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Heat number'),
        ),
        migrations.AddField(
            model_name='raceheat',
            name='started_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Heat started time'),
        ),
        migrations.AlterField(
            model_name='heatevent',
            name='heat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triggered_events', to='races.RaceHeat'),
        ),
        migrations.AlterField(
            model_name='heatevent',
            name='tracker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='triggered_events', to='trackers.Tracker'),
        ),
        migrations.AlterField(
            model_name='heatevent',
            name='trigger',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Gate Trigger'), (1, 'Area Entered Trigger'), (2, 'Area Exit Trigger'), (3, 'Crash Trigger'), (4, 'Land Trigger'), (5, 'Takeoff Trigger'), (6, 'Arm Trigger'), (7, 'Disarm Trigger'), (8, 'Start Trigger'), (9, 'End Trigger')], verbose_name='trigger'),
        ),
        migrations.AlterUniqueTogether(
            name='raceheat',
            unique_together=set([('number', 'event')]),
        ),
    ]
