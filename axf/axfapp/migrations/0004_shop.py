# Generated by Django 2.2.1 on 2019-05-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfapp', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
