# Generated by Django 3.2.9 on 2022-01-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(default='PORVOO', max_length=255),
        ),
    ]
