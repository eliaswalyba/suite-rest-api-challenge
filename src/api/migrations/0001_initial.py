# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cellphone', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GeoPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('alt', models.FloatField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('geopoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GeoPoint')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('geopoint', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.GeoPoint')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Menu'),
        ),
    ]
