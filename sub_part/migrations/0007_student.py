# Generated by Django 4.1.4 on 2023-03-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_image_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]
