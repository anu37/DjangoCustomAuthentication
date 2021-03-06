# Generated by Django 3.0.6 on 2020-05-24 12:45

import customauth.generators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, default=customauth.generators.generate_client_id, max_length=100, unique=True)),
                ('client_secret', models.CharField(db_index=True, default=customauth.generators.generate_client_id, max_length=100, unique=True)),
                ('application_name', models.CharField(max_length=255)),
                ('activate', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('access_token', models.CharField(max_length=100, unique=True)),
                ('refresh_token', models.CharField(max_length=100, unique=True)),
                ('expiry_date', models.DateTimeField()),
                ('refresh_token_expiry', models.DateTimeField()),
                ('expired', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='app_name', serialize=False, to='customauth.Application')),
            ],
        ),
    ]
