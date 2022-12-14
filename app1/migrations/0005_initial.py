# Generated by Django 4.1.1 on 2022-10-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0004_delete_booksinf'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=64)),
                ('bauthor', models.CharField(max_length=32)),
                ('bimg', models.CharField(max_length=1024)),
                ('bstate', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
