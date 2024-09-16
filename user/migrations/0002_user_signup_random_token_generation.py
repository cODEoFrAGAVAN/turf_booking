# Generated by Django 5.1.1 on 2024-09-13 17:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_signup',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('mailid', models.EmailField(max_length=50, unique=True)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Random_token_generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('random_token', models.CharField(max_length=200)),
                ('mobile_number', models.ForeignKey(default='0000000000', on_delete=django.db.models.deletion.CASCADE, to='user.user_signup')),
            ],
        ),
    ]
