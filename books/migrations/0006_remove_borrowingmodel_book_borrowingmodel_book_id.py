# Generated by Django 5.0.6 on 2024-07-08 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_borrowingmodel_book_id_borrowingmodel_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowingmodel',
            name='book',
        ),
        migrations.AddField(
            model_name='borrowingmodel',
            name='book_id',
            field=models.IntegerField(null=True),
        ),
    ]
