# Generated by Django 3.1.4 on 2020-12-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_generation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='LiveEvent',
        ),
    ]
