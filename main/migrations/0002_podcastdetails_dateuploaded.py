# Generated by Django 4.2 on 2023-04-22 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastdetails',
            name='dateuploaded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Uploaded'),
            preserve_default=False,
        ),
    ]
