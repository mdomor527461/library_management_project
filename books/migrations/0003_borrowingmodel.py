# Generated by Django 5.0.6 on 2024-07-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_bookmodels_bookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
