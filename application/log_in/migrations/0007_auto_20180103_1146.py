# Generated by Django 2.0 on 2018-01-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0006_auto_20180103_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlogs',
            name='agent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
