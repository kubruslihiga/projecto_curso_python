# Generated by Django 2.2.2 on 2019-06-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
