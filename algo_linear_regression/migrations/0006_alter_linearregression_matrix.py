# Generated by Django 3.2.4 on 2021-07-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo_linear_regression', '0005_rename_linear_regression_column_algorithm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linearregression',
            name='matrix',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]