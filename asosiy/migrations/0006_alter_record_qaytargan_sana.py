# Generated by Django 4.1.5 on 2023-01-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_alter_admin_ish_vaqti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='qaytargan_sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
