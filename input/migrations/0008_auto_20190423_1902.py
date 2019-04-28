# Generated by Django 2.2 on 2019-04-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0007_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('video', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'videoinfo',
            },
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]