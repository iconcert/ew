# Generated by Django 3.2.3 on 2021-05-27 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_weight', models.BooleanField()),
                ('enter_manually', models.BooleanField()),
                ('name', models.CharField(max_length=50, verbose_name='Название посылки')),
                ('tracking_number', models.CharField(max_length=50, verbose_name='Трекинг номер')),
                ('status', models.CharField(choices=[('1', 'Проверяется'), ('2', 'Ждем на склад'), ('3', 'На складе'), ('4', 'Отправлена'), ('5', 'На обработке'), ('6', 'Прибыла в Бишкек'), ('7', 'Доставлена заказчику'), ('8', 'Неправильный трек-номер'), ('9', 'Возвращена отправителю'), ('10', 'Задержана на складе'), ('11', 'Отменена')], default='1', max_length=2)),
                ('warehouse', models.CharField(choices=[('1', 'США'), ('2', 'Турция'), ('3', 'Россия')], default='1', max_length=2)),
                ('comment', models.TextField(blank=True)),
                ('photo_parcel', models.ImageField(blank=True, default='', upload_to='parcels/photos/%Y/%m/%d/', verbose_name='Фотография посылки')),
                ('photo_label', models.ImageField(blank=True, default='', upload_to='parcels/photos/%Y/%m/%d/', verbose_name='Фотография лейбла')),
                ('photo_repackaging', models.ImageField(blank=True, default='', upload_to='parcels/photos/%Y/%m/%d/', verbose_name='Фотография после переупаковки')),
                ('photo_order', models.ImageField(blank=True, default='', upload_to='parcels/photos/%Y/%m/%d/', verbose_name='Фотография заказа')),
                ('date_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('date_sent', models.DateTimeField(blank=True, null=True)),
                ('date_arrived', models.DateTimeField(blank=True, null=True)),
                ('date_delivered', models.DateTimeField(blank=True, null=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='parcels.store')),
                ('user_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Посылка',
                'verbose_name_plural': 'Посылки',
            },
        ),
    ]
