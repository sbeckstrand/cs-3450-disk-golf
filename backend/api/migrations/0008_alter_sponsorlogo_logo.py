# Generated by Django 3.2.9 on 2021-11-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_sponsorlogo_sponsor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorlogo',
            name='logo',
            field=models.ImageField(upload_to='logos'),
        ),
    ]
