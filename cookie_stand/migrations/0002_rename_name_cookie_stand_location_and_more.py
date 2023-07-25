# Generated by Django 4.1.5 on 2023-07-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stand', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie_stand',
            old_name='name',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='cookie_stand',
            old_name='reviewer',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cookie_stand',
            name='rating',
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='hourly_sales',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cookie_stand',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]