# Generated by Django 4.2.2 on 2023-06-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteadmin', '0005_borrowbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='returnbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberid', models.IntegerField()),
                ('bookBorrow', models.CharField(max_length=100)),
                ('bookid', models.CharField(max_length=10)),
                ('returnDate', models.DateField()),
                ('lateDate', models.IntegerField()),
                ('fine', models.IntegerField()),
            ],
        ),
    ]
