# Generated by Django 3.1.4 on 2020-12-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201218_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='sss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss_title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('sss_content', models.CharField(max_length=500, verbose_name='İçeriği')),
            ],
        ),
    ]
