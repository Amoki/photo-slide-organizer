# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_auto_20160226_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='motcle',
            name='categorie',
            field=models.ManyToManyField(blank=True, to='photo.Categorie'),
        ),
    ]
