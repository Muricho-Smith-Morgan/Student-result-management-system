# Generated by Django 4.1.2 on 2021-07-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
            ],
        ),
    ]
