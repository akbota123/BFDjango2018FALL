# Generated by Django 2.1.1 on 2018-09-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(default=10),
        ),
    ]
