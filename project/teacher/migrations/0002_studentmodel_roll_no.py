# Generated by Django 4.1.5 on 2023-01-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='roll_no',
            field=models.IntegerField(null=True),
        ),
    ]
