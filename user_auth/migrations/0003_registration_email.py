# Generated by Django 4.2.4 on 2024-08-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_registration_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(default='', max_length=150, unique=True),
        ),
    ]
