# Generated by Django 4.1 on 2023-02-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Famale')], max_length=30),
        ),
    ]
