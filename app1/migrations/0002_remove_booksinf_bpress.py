# Generated by Django 4.1.1 on 2022-10-01 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksinf',
            name='bpress',
        ),
    ]
