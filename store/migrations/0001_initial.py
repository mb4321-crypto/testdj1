# Generated by Django 5.1.6 on 2025-02-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1050)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'coffee',
            },
        ),
    ]
