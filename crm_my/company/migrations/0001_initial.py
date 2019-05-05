# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-04-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='课程名')),
                ('intro', models.CharField(blank=True, max_length=32, null=True, verbose_name='简介')),
                ('cycle', models.CharField(blank=True, max_length=32, null=True, verbose_name='课程周期')),
                ('lecturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='讲师')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=32, null=True, verbose_name='城市')),
                ('area', models.CharField(blank=True, max_length=32, null=True, verbose_name='地区')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='教室名')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, default=None, help_text='格式yyyy-mm-dd', null=True, verbose_name='出生日期')),
                ('qq', models.CharField(help_text='QQ号必须唯一', max_length=64, unique=True, verbose_name='QQ')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='手机号')),
                ('course', models.ForeignKey(default='未选择课程', on_delete=django.db.models.deletion.CASCADE, to='company.Course')),
                ('room', models.ForeignKey(default='未选择教室', on_delete=django.db.models.deletion.CASCADE, to='company.Room')),
            ],
        ),
    ]
