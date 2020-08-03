# Generated by Django 3.0.8 on 2020-07-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('carousel_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('carousel_url', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(max_length=100)),
                ('carousel_rand', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=0)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_carousel',
            },
        ),
    ]