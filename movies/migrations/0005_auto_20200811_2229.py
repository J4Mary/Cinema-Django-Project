# Generated by Django 3.0.6 on 2020-08-11 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200810_2047'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seance',
            unique_together={('id', 'beginning', 'hall')},
        ),
    ]