# Generated by Django 5.1.7 on 2025-03-24 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=50)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=750)),
                ('forum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forums.forum')),
            ],
        ),
    ]
