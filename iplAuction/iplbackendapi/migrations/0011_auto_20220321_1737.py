# Generated by Django 3.2.9 on 2022-03-21 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplbackendapi', '0010_playing11_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='retainedBy',
            field=models.CharField(default='RCB', max_length=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.FloatField(default=100.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
