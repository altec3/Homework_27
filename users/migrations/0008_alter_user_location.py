# Generated by Django 4.1.3 on 2022-11-13 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_alter_location_lat_alter_location_lng'),
        ('users', '0007_alter_user_age_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='locations.location'),
        ),
    ]
