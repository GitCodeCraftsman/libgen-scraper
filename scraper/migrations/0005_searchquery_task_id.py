# Generated by Django 4.2 on 2024-04-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_searchquery_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='task_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]