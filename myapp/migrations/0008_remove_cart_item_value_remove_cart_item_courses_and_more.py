# Generated by Django 5.0.7 on 2024-09-25 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_user_cart_item_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='Value',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='cart_item',
        ),
    ]
