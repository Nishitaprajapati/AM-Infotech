# Generated by Django 4.0.5 on 2023-02-26 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_order_details_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
