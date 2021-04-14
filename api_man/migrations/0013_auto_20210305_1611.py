# Generated by Django 3.1.7 on 2021-03-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_man', '0012_auto_20210305_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apimodel',
            old_name='last_edit_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='baseurlmodel',
            old_name='last_edit_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='projectmodel',
            old_name='last_edit_time',
            new_name='create_time',
        ),
        migrations.AlterField(
            model_name='apimodel',
            name='flag',
            field=models.CharField(choices=[('1', '执行'), ('2', '不执行')], max_length=10, verbose_name='是否执行该接口'),
        ),
    ]