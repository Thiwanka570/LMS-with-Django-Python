# Generated by Django 4.2.2 on 2023-06-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteadmin', '0004_member_alter_books_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrowbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberid', models.IntegerField()),
                ('bookid', models.IntegerField()),
                ('book', models.CharField(max_length=100)),
                ('member', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('borrowdate', models.DateField()),
                ('returndate', models.DateField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
