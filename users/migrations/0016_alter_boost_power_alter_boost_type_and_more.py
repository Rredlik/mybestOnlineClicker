# Generated by Django 4.0.3 on 2022-06-01 11:07

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_core_auto_click_power_alter_core_click_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='power',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'auto'), (0, 'casual')], default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='auto_click_power',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='click_power',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='core',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Такой пользователь уже зарегестрирован.'}, help_text='', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]