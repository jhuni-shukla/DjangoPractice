# Generated by Django 5.0.3 on 2024-04-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_IS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('edept', models.CharField(max_length=100)),
                ('ephone', models.IntegerField()),
                ('eemail', models.CharField(max_length=100)),
                ('eaddress', models.CharField(max_length=100)),
                ('esalary', models.IntegerField()),
            ],
        ),
    ]
