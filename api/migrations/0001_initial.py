# Generated by Django 5.1.1 on 2024-10-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=205)),
                ('category', models.CharField(max_length=205)),
                ('isCredit', models.BooleanField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]