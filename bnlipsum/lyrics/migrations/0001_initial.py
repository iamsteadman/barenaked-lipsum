# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('artwork', models.ImageField(upload_to=b'albums')),
            ],
            options={
                'ordering': ('year', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Stanza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('lyrics', models.TextField()),
                ('chorus', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('number', 'track'),
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='lyrics.Album')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.AddField(
            model_name='stanza',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stanzas', to='lyrics.Track'),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([('number', 'album')]),
        ),
    ]
