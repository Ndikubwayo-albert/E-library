# Generated by Django 4.1.7 on 2023-03-22 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 18, 36, 2, 289730, tzinfo=datetime.timezone.utc)),
        ),
    ]