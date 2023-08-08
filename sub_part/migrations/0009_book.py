# Generated by Django 4.1.4 on 2023-03-08 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_student_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('page', models.IntegerField()),
                ('auther', models.CharField(max_length=100)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_part.student')),
            ],
        ),
    ]
