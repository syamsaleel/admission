# Generated by Django 4.2.2 on 2023-06-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(blank=True, max_length=10)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('class_level', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('marklist', models.FileField(blank=True, null=True, upload_to='marklists/')),
            ],
        ),
    ]