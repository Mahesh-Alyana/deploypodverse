# Generated by Django 4.2 on 2023-04-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_podcastdetails_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastdetails',
            name='likes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Likes'),
        ),
    ]
