# Generated by Django 5.0.4 on 2024-05-02 17:28

import timezone_field.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_boys_timezone_alter_girls_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boys',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Asia/Bishkek'),
        ),
        migrations.AlterField(
            model_name='girls',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Asia/Bishkek'),
        ),
    ]
