# Generated by Django 4.0.5 on 2022-07-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
