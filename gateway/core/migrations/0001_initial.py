# Generated by Django 4.1 on 2022-08-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('request_path', models.CharField(max_length=255)),
                ('upstream_url', models.CharField(max_length=255)),
            ],
        ),
    ]
