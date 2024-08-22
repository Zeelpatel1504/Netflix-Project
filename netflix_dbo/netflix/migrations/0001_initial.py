# Generated by Django 5.0.3 on 2024-03-31 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'netflix_users',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('GID', models.AutoField(primary_key=True, serialize=False)),
                ('GName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('LID', models.AutoField(primary_key=True, serialize=False)),
                ('LName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('PID', models.AutoField(primary_key=True, serialize=False)),
                ('PName', models.CharField(max_length=255)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.genre')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.profile')),
            ],
            options={
                'unique_together': {('profile', 'genre')},
            },
        ),
    ]