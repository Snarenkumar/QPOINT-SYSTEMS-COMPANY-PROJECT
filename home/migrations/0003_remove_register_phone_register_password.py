# Generated by Django 4.2.5 on 2023-09-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
