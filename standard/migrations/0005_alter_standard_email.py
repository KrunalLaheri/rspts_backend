# Generated by Django 4.0.6 on 2022-08-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0004_rename_standard_email_standard_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
