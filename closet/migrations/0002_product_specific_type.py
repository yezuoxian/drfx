# Generated by Django 2.2.1 on 2019-05-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specific_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
