# Generated by Django 2.2.5 on 2019-09-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]