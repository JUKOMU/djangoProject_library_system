# Generated by Django 4.1.1 on 2022-10-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_delete_userinf'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]