# Generated by Django 4.0.2 on 2022-02-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_remove_clients_email_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='email_client',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
