# Generated by Django 4.0.2 on 2022-02-17 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_clients_lawyer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='lawyer_name',
        ),
    ]
