# Generated by Django 4.1.7 on 2023-02-28 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('creation_date', models.DateTimeField(auto_created=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=64)),
                ('company', models.TextField()),
                ('job', models.TextField()),
            ],
        ),
    ]
