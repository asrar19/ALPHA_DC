# Generated by Django 4.1.7 on 2023-03-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default=None, max_length=512),
            preserve_default=False,
        ),
    ]
