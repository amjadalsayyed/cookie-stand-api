# Generated by Django 4.1.5 on 2023-07-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stand', '0002_rename_name_cookie_stand_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie_stand',
            old_name='location',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cookie_stand',
            old_name='owner',
            new_name='reviewer',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='average_cookies_per_sale',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='hourly_sales',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='maximum_customers_per_hour',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='minimum_customers_per_hour',
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
