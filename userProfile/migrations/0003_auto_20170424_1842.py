# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20170419_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='languages',
            options={'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
        migrations.AlterField(
            model_name='languages',
            name='languageName',
            field=models.TextField(max_length=30, verbose_name='Language name'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='localeCode',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Language Code'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='localeCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Languages', verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=15, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobileVerified',
            field=models.BooleanField(default=False, verbose_name='Mobile Verified'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='UserID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userName',
            field=models.CharField(blank=True, max_length=30, verbose_name='User Name'),
        ),
    ]