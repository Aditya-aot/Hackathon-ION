# Generated by Django 3.2.7 on 2022-01-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220126_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='crypto_port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.TextField(null=True)),
                ('quantity', models.TextField(null=True)),
            ],
        ),
    ]
