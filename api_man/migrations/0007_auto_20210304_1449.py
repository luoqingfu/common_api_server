# Generated by Django 3.1.7 on 2021-03-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_man', '0006_auto_20210304_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimodel',
            name='project',
            field=models.CharField(max_length=10, verbose_name='所属项目'),
        ),
    ]
