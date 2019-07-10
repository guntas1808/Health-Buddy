# Generated by Django 2.2.3 on 2019-07-08 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_auto_20190708_0325'),
        ('seven', '0004_auto_20190708_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('test', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
        migrations.DeleteModel(
            name='bodyVital',
        ),
    ]
