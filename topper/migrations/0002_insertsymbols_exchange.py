# Generated by Django 4.1.3 on 2022-11-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insertsymbols',
            name='exchange',
            field=models.CharField(default='NSE', max_length=50),
        ),
    ]