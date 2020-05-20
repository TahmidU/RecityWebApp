# Generated by Django 3.0.3 on 2020-02-21 15:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]