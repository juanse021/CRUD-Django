# Generated by Django 2.1 on 2018-10-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
