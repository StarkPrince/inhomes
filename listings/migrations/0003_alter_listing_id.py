# Generated by Django 5.1.1 on 2024-12-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210707_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]