# Generated by Django 5.0.6 on 2024-05-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
