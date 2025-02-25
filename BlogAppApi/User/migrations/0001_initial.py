# Generated by Django 5.0.7 on 2024-07-29 13:25

import User.api.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogger_phone_code', models.CharField(blank=True, max_length=5, null=True, validators=[User.api.validators.validate_phone_code])),
                ('blogger_phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[User.api.validators.validate_phone_number])),
                ('blogger_organization', models.CharField(blank=True, max_length=100, null=True)),
                ('blogger_bio', models.CharField(blank=True, max_length=500, null=True)),
                ('blogger_IsVerified', models.BooleanField(default=False)),
                ('blogger_joined', models.DateTimeField(auto_now_add=True)),
                ('blogger_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blogOwnerUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bloggers',
            },
        ),
    ]
