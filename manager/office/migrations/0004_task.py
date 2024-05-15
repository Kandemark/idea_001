# Generated by Django 5.0.4 on 2024-04-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_promotedemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_of_submition', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
