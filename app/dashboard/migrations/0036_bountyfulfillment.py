# Generated by Django 2.0 on 2018-01-30 02:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_auto_20180129_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='BountyFulfillment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('github_username', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('bounty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Bounty')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]