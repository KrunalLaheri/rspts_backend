# Generated by Django 4.0.6 on 2022-08-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_profilephoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profilePhoto',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
