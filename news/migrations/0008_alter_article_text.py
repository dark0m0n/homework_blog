# Generated by Django 4.2 on 2023-04-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
