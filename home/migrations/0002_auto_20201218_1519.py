# Generated by Django 3.1.4 on 2020-12-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='musteri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis', models.CharField(max_length=5, verbose_name='Tpplam Satış')),
                ('puan', models.CharField(max_length=5, verbose_name='Puan')),
                ('musteri', models.CharField(max_length=5, verbose_name='Müşteri')),
                ('ürün', models.CharField(max_length=5, verbose_name='Ürün')),
            ],
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_1',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 1'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_2',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 2'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_3',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 3'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_4',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 4'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_5',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 5'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_6',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 6'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_7',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 7'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_8',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 8'),
        ),
        migrations.AlterField(
            model_name='paket',
            name='paket_9',
            field=models.CharField(blank=True, max_length=25, verbose_name='Paket Özelliği 9'),
        ),
    ]