# Generated by Django 2.2.24 on 2023-04-27 09:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230427_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО владельца')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, verbose_name='Исправленный номер телефона')),
                ('flats', models.ManyToManyField(blank=True, default=None, related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности:')),
            ],
        ),
    ]