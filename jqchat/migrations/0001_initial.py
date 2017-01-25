# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-25 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField(blank=True, choices=[(1, b"has changed the room's description."), (2, b'has joined the room.'), (3, b'has left the room.')], help_text=b'An action performed in the room, either by a user or by the system (e.g. XYZ leaves room.', null=True)),
                ('text', models.TextField(blank=True, help_text=b'A message, either typed in by a user or generated by the system.', null=True)),
                ('unix_timestamp', models.FloatField(editable=False, help_text=b'Unix timestamp when this message was inserted into the database.')),
                ('created', models.DateTimeField(editable=False)),
            ],
            options={
                'ordering': ['unix_timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text=b'Name of the room.', max_length=255, null=True)),
                ('created', models.DateTimeField(editable=False)),
                ('description', models.CharField(blank=True, help_text=b'The description of this room.', max_length=100, null=True)),
                ('description_modified', models.IntegerField(editable=False, help_text=b'Unix timestamp when the description was created or last modified.', null=True)),
                ('last_activity', models.IntegerField(editable=False, help_text=b'Last activity in the room. Stored as a Unix timestamp.')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(help_text=b'This message was posted in a given chat room.', on_delete=django.db.models.deletion.CASCADE, to='jqchat.Room'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jchat_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
