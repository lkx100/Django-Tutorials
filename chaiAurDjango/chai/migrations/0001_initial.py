# Generated by Django 5.0.7 on 2024-07-28 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chaiVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chai_images/')),
                ('date_added', models.DateTimeField(default=datetime.datetime(2024, 7, 28, 16, 26, 43, 877153, tzinfo=datetime.timezone.utc))),
                ('chaiType', models.CharField(choices=[('GT', 'Green Tea'), ('MS', 'Masala Chai'), ('BT', 'Black Tea'), ('MC', 'Malai Chai'), ('GR', 'Ginger Tea')], max_length=2)),
            ],
        ),
    ]
