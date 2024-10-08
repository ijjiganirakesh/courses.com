# Generated by Django 5.0.7 on 2024-09-24 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.account')),
            ],
        ),
    ]
