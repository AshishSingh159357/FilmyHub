# Generated by Django 3.0.6 on 2020-05-26 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filmyhub_app', '0002_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
    ]