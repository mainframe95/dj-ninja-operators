# Generated by Django 4.0.1 on 2022-01-13 13:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('isActive', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]