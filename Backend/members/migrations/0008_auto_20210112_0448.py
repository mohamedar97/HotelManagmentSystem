# Generated by Django 2.2.10 on 2021-01-12 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20210111_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.Payment'),
        ),
    ]
