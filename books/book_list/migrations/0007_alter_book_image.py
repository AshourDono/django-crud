# Generated by Django 4.0.4 on 2022-04-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0006_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='book_list/static/book_list/images/1.jpg', null=True, upload_to='book_list/static/book_list/images'),
        ),
    ]
