# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('image', models.ImageField(blank=True, upload_to='img/%Y/%m/%d', verbose_name='Image')),
                ('body', models.TextField(verbose_name='Comment')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent_post', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='post.Post')),
                ('parent_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='thread.Thread')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
