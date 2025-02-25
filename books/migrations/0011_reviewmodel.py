# Generated by Django 5.0.6 on 2024-07-08 05:59

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_borrowingmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=books.models.BookModel, related_name='reviews', to='books.bookmodel')),
            ],
        ),
    ]
