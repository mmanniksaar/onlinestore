# Generated by Django 3.2.9 on 2022-01-22 20:58

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='58.91599192355906,25.400390625', max_length=63),
        ),
    ]
