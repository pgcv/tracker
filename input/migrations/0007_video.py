# Generated by Django 2.2 on 2019-04-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0006_remove_userinfo_videofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]