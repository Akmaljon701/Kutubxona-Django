# Generated by Django 4.1.5 on 2023-01-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_rename_bitriruvchi_talaba_bitruvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='qaytargan_sana',
            field=models.DateField(null=True),
        ),
    ]
