# Generated by Django 3.2.6 on 2023-03-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
            ],
        ),
    ]