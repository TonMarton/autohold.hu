# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='alufelni',
            field=models.CharField(blank=True, choices=[('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='belső_szín',
            field=models.CharField(blank=True, choices=[('sötét', 'Sötét'), ('világos', 'Világos')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='belső_szín_részletes',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='csomagtartó',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='elsőforgalomba',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='futott',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='hajtás',
            field=models.CharField(blank=True, choices=[('Elsőkerék', 'Elsőkerék'), ('Hátsókerék', 'Hátsókerék'), ('Állítható-összkerék', 'Állítható-összkerék'), ('Állandó-összkerék', 'Állandó-összkerék')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='hangszórók_száma',
            field=models.CharField(blank=True, choices=[('2', '2'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='henger_elrendezés',
            field=models.CharField(blank=True, choices=[('Soros-Álló', 'Soros-Álló'), ('Soros-Fekvő', 'Soros-Fekvő'), ('V', 'V'), ('Boxer', 'Boxer'), ('W', 'W'), ('Wankel', 'Wankel')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='klíma_fajta',
            field=models.CharField(blank=True, choices=[('Automata', 'Automata'), ('Digitális', 'Digitális'), ('Digitális-kétzónás', 'Digitális-kétzónás'), ('Digitális-többzónás', 'Digitális-többzónás')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='környezetvédelmi_osztály',
            field=models.CharField(blank=True, choices=[('15', '15'), ('14', '14'), ('13', '13'), ('12', '12'), ('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='külső_szín',
            field=models.CharField(blank=True, choices=[('sötét', 'Sötét'), ('világos', 'Világos')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='külső_szín_részletes',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='leírás',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='motorűrtartam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='saját_tömeg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='seb_váltó_fajta',
            field=models.CharField(blank=True, choices=[('Automata', 'Automata'), ('Félautomata', 'Félautomata'), ('Fokozatmentes-Automata', 'Fokozatmentes-Automata'), ('Szekvenciális', 'Szekvenciális'), ('Tiptronic', 'Tiptronic')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='teljesítmény',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='tető_fajta',
            field=models.CharField(blank=True, choices=[('Lemeztető', 'Lemeztető'), ('Vászontető', 'Vászontető'), ('Nyitható keménytető', 'Nyitható keménytető'), ('Harmonikatető', 'Harmonikatető'), ('Targatető', 'Targatető'), ('Fix üvegtető', 'Fix üvegtető'), ('Panoráma tető', 'Panoráma tető'), ('Fix napfénytető', 'Fix napfénytető'), ('Nyitható napfénytető', 'Nyitható napfénytető'), ('Elhúzható napfénytető', 'Elhúzható napfénytető'), ('Motoros napfénytető', 'Motoros napfénytető')], max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='ár',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='évjárat',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='össztömeg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='üzemanyagtípus',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
