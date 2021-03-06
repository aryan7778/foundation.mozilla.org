# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-02 18:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import networkapi.buyersguide.models
import networkapi.buyersguide.validators


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0004_auto_20181002_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanProductVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('attribute', models.CharField(max_length=100, validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=['confidence'])])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooleanVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=100, validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=['confidence'])])),
                ('value', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BooleanVoteBreakdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('bucket', models.IntegerField(validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=[0, 1])])),
                ('product_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyersguide.BooleanProductVote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RangeProductVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('attribute', models.CharField(max_length=100, validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=['creepiness'])])),
                ('average', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RangeVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=100, validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=['creepiness'])])),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RangeVoteBreakdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('bucket', models.IntegerField(validators=[networkapi.buyersguide.validators.ValueListValidator(valid_values=[0, 1, 2, 3, 4])])),
                ('product_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyersguide.RangeProductVote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, help_text='Image representing this product', max_length=2048, upload_to=networkapi.buyersguide.models.get_product_image_upload_path),
        ),
        migrations.AddField(
            model_name='rangevote',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyersguide.Product'),
        ),
        migrations.AddField(
            model_name='rangeproductvote',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='range_product_votes', to='buyersguide.Product'),
        ),
        migrations.AddField(
            model_name='booleanvote',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyersguide.Product'),
        ),
        migrations.AddField(
            model_name='booleanproductvote',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_product_votes', to='buyersguide.Product'),
        ),
    ]
