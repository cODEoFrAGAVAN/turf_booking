# Generated by Django 5.1.1 on 2024-09-13 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_signup_random_token_generation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='random_token_generation',
            old_name='mobile_number',
            new_name='mobile',
        ),
    ]
