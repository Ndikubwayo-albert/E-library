# Generated by Django 4.1.7 on 2023-03-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_alter_author_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dateofbirth',
            field=models.DateTimeField(auto_created=True),
        ),
    ]