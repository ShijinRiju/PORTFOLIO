# Generated by Django 5.0.6 on 2024-05-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PORTFOLIO_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
