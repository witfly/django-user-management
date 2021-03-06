# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='authtoken', on_delete=models.CASCADE),
        ),
    ]
