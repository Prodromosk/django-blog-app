# Generated by Django 2.0.2 on 2018-02-25 17:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180225_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 25, 17, 36, 55, 704104, tzinfo=utc)),
        ),
    ]
