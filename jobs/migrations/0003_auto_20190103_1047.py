# Generated by Django 2.0.5 on 2019-01-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190103_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='summary',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]