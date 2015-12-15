# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetterThan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='betterthan',
            name='better_than',
            field=models.ForeignKey(related_name='better_than_rel', to='images.Image'),
        ),
        migrations.AddField(
            model_name='betterthan',
            name='worse_than',
            field=models.ForeignKey(related_name='worse_than_rel', to='images.Image'),
        ),
    ]
