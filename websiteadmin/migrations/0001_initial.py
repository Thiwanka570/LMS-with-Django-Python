# Generated by Django 4.2.2 on 2023-06-21 16:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addbook',
            fields=[
                ('bookid', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]