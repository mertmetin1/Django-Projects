# Generated by Django 5.0.7 on 2024-07-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_keywords',
            field=models.TextField(),
        ),
    ]
