# Generated by Django 3.1.7 on 2021-04-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guru', '0002_db_mprof'),
    ]

    operations = [
        migrations.CreateModel(
            name='assign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Topic', models.CharField(max_length=50)),
                ('Assignment', models.CharField(max_length=200)),
            ],
        ),
    ]