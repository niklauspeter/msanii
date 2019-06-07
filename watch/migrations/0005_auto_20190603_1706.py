# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-03 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0004_auto_20190603_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='tags',
        ),
        migrations.AlterField(
            model_name='authorities',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='health',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood'),
        ),
    ]
