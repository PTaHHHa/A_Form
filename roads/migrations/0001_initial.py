# Generated by Django 3.1.4 on 2020-12-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenAppeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(blank=True, max_length=120, null=True, verbose_name='Фамилия Имя Отчество')),
                ('organisation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование организации')),
                ('address', models.CharField(max_length=120, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=120, null=True, verbose_name='Email для обратной связи')),
                ('text', models.TextField(max_length=900, null=True, verbose_name='Сообщение для нас')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationAppeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=120, null=True, verbose_name='ФИО уполномоченного представителя')),
                ('organisation', models.CharField(max_length=50, null=True, verbose_name='Наименование юридического лица')),
                ('address', models.CharField(max_length=120, null=True, verbose_name='Адрес юридического лица')),
                ('email', models.EmailField(max_length=120, null=True, verbose_name='Email для обратной связи')),
                ('text', models.TextField(max_length=900, null=True, verbose_name='Сообщение для нас')),
            ],
        ),
    ]
