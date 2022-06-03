# Generated by Django 4.0.2 on 2022-02-17 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_remove_clients_lawyer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='lawyer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.employees'),
        ),
    ]
