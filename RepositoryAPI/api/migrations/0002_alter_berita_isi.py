# Generated by Django 3.2.8 on 2022-01-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='isi',
            field=models.TextField(),
        ),
    ]
