# Generated by Django 4.0.2 on 2022-02-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_employees_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=30)),
                ('information', models.TextField(default='', max_length=600)),
            ],
        ),
    ]
