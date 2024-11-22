# Generated by Django 4.2 on 2024-11-22 19:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('status', models.BooleanField(verbose_name='Проживает')),
                ('arrival_date', models.DateField(verbose_name='Дата прибытья')),
                ('departure_date', models.DateField(verbose_name='Дата отбытья')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{10,15}$', 'Введите корректный номер телефона из 10-15 цифр')])),
                ('place_of_study', models.CharField(max_length=200, verbose_name='Место учебы')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('room', models.IntegerField(verbose_name='Комната')),
                ('photo_of_passport', models.ImageField(blank=True, upload_to='passport_photos/', verbose_name='Фото паспорта')),
                ('photo_of_student', models.ImageField(blank=True, upload_to='student_photos/', verbose_name='Фото студента')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(verbose_name='Дата оплаты')),
                ('payed_to_this_month', models.BooleanField(verbose_name='Оплачено на этот месяц')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО Родителя')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{10,15}$', 'Введите корректный номер телефона из 10-15 цифр')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='main.student')),
            ],
        ),
    ]
