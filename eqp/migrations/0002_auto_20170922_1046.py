# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-22 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eqp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_box',
            name='box_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eqp.tbl_qr_code', verbose_name='二维ID'),
        ),
    ]
