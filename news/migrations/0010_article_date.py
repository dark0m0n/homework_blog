# Generated by Django 4.2 on 2023-04-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]