# Generated by Django 4.2 on 2024-11-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservalo_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicleta',
            name='imagen',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.8mLUw63EOxbQI8r_7SgRIQHaHa?w=193&h=192&c=7&r=0&o=5&dpr=1.3&pid=1.7', max_length=500),
        ),
    ]
