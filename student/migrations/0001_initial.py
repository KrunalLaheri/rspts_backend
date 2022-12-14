# Generated by Django 4.0.6 on 2022-08-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('school_id', models.CharField(blank=True, max_length=100, null=True)),
                ('standard_id', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=250)),
                ('admission_date', models.DateField()),
                ('result', models.JSONField(default={'Subject name': 'Subject Marks'}, null=True)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usertoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
            ],
        ),
    ]
