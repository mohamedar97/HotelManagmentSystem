# Generated by Django 2.2.10 on 2021-01-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_booking_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]