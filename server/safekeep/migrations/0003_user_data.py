# Generated by Django 3.2.4 on 2021-06-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('safekeep', '0002_delete_user_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=20)),
                ('workingHours', models.IntegerField()),
                ('deleteStatus', models.BooleanField(default=False)),
            ],
        ),
    ]
