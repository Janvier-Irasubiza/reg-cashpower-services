# Generated by Django 5.0.6 on 2024-05-17 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_dispense_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('id_card_number', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='request',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.client'),
        ),
    ]
