# Generated by Django 2.0.5 on 2019-01-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20190103_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
