# Generated by Django 4.0.4 on 2022-04-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='add_to_site_at',
            field=models.DateField(auto_created=True, db_column='Added At', null=True),
        ),
    ]
