# Generated by Django 2.2.1 on 2019-06-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_restaurantprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='desc',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
