# Generated by Django 5.1.4 on 2024-12-12 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contact_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 12, 16, 23, 50, 229818)),
        ),
    ]
