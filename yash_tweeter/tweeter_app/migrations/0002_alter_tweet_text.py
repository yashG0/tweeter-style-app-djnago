# Generated by Django 5.0.7 on 2024-08-03 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
