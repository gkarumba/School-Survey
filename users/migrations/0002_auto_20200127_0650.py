# Generated by Django 2.2.3 on 2020-01-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=2550),
        ),
    ]