# Generated by Django 4.0.2 on 2022-02-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_clients_email_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]