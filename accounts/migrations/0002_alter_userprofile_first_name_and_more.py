# Generated by Django 4.2.17 on 2024-12-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]