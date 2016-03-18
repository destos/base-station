# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 04:25
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import recurrence.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start', models.DateTimeField(verbose_name='Start time')),
                ('end', models.DateTimeField(verbose_name='End time')),
                ('title_template', models.TextField(blank=True, help_text='jinja2 template used to render occurrence titles', null=True)),
                ('description_template', models.TextField(blank=True, help_text='jinja2 template used to render occurrence descriptions', null=True)),
                ('recurrences', recurrence.fields.RecurrenceField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalEvent',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('start', models.DateTimeField(verbose_name='Start time')),
                ('end', models.DateTimeField(verbose_name='End time')),
                ('title_template', models.TextField(blank=True, help_text='jinja2 template used to render occurrence titles', null=True)),
                ('description_template', models.TextField(blank=True, help_text='jinja2 template used to render occurrence descriptions', null=True)),
                ('recurrences', recurrence.fields.RecurrenceField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical event',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalEventTemplate',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical event template',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Location Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Address')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location')),
                ('location_hash', models.CharField(max_length=32, null=True)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='metadata')),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('start', models.DateTimeField(verbose_name='Start time')),
                ('end', models.DateTimeField(verbose_name='End time')),
                ('original_start', models.DateTimeField(verbose_name='Original start')),
                ('original_end', models.DateTimeField(verbose_name='Original end')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Cancelled')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrences', to='events.Event', verbose_name='Event')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Location')),
            ],
            options={
                'ordering': ('start',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='location',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='events.Location'),
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='template',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='events.EventTemplate'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventTemplate'),
        ),
    ]
