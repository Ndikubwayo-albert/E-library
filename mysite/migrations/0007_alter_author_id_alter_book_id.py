# Generated by Django 4.1.7 on 2023-03-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_author_alter_book_author_alter_book_book_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]