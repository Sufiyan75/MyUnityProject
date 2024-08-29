# Generated by Django 4.2.4 on 2024-08-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='education_details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='hobby',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='mobile',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='skills',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]