# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('chair', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lims_number', models.CharField(max_length=30)),
                ('actions_date', models.DateField(null=True, blank=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('issues', models.TextField(default=b'', null=True, blank=True)),
                ('referral', models.ManyToManyField(to='app.Committee', null=True, verbose_name=b'Committee Referral', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
