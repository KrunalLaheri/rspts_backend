# Generated by Django 4.0.6 on 2022-08-22 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_rename_admission_date_student_admissiondate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='studentId',
        ),
    ]