# Generated by Django 2.2.2 on 2019-06-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20190623_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='soft_copy',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
