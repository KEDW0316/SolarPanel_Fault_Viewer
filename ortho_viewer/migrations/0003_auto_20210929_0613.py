# Generated by Django 3.2.7 on 2021-09-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ortho_viewer', '0002_auto_20210929_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel_fault',
            name='px_x',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='panel_fault',
            name='px_y',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
