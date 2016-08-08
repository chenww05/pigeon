# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'start_time', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'end_time', blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('budget', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('cost', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('start_date', models.DateTimeField(verbose_name=b'sign up date')),
                ('last_edit_date', models.DateTimeField(verbose_name=b'sign up date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('signup_date', models.DateTimeField(verbose_name=b'sign up date')),
                ('has_sign_up', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='planner.User')),
                ('business_name', models.CharField(max_length=200)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=('planner.user',),
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('budget', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('cost', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('start_date', models.DateTimeField(null=True, verbose_name=b'start date', blank=True)),
                ('wedding_date', models.DateTimeField(null=True, verbose_name=b'wedding date', blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('venue', models.CharField(max_length=200, null=True, blank=True)),
                ('guest_list', models.ManyToManyField(related_name=b'wedding_guest', null=True, to='planner.User', blank=True)),
                ('note_list', models.ManyToManyField(related_name=b'wedding_note', null=True, to='planner.Note', blank=True)),
                ('spouse', models.ForeignKey(related_name=b'wedding_owner', to='planner.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='guest_list',
            field=models.ManyToManyField(related_name=b'event_guest', null=True, to='planner.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='helper_list',
            field=models.ManyToManyField(related_name=b'event_helper', null=True, to='planner.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(related_name=b'event_owner', to='planner.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='service_provider_list',
            field=models.ManyToManyField(related_name=b'event_service_provider', null=True, to='planner.ServiceProvider', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='wedding',
            field=models.ForeignKey(to='planner.Wedding'),
            preserve_default=True,
        ),
    ]
