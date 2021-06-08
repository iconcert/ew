from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Parcel(models.Model):
    STATUS_CHOICES = (
        ('1', 'Проверяется'),
        ('2', 'Ждем на склад'),
        ('3', 'На складе'),
        ('4', 'Отправлена'),
        ('5', 'На обработке'),
        ('6', 'Прибыла'),
        ('7', 'Доставлена заказчику'),
        ('8', 'Неправильный трек-номер'),
        ('9', 'Возвращена отправителю'),
        ('10', 'Задержана на складе'),
        ('11', 'Отменена'),
    )
    WAREHOUSE_CHOICES = (
        ('1', 'США'),
        ('2', 'Турция'),
        ('3', 'Россия'),
    )
    volume_weight = models.BooleanField()
    enter_manually = models.BooleanField()

    name = models.CharField('Название посылки', max_length=50)

    store = models.ForeignKey('Store', on_delete=models.PROTECT, null=True)
    tracking_number = models.CharField('Трекинг номер', max_length=50)

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='1')
    warehouse = models.CharField(max_length=2, choices=WAREHOUSE_CHOICES, default='2')

    comment = models.TextField(blank=True)

    user_warehouse = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')
    user_client = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')

    photo_parcel = models.ImageField('Фотография посылки', upload_to='images/parcels/%Y/%m/%d/', default='', blank=True)
    photo_label = models.ImageField('Фотография лейбла', upload_to='images/parcels/%Y/%m/%d/', default='', blank=True)
    photo_repackaging = models.ImageField('Фотография после переупаковки', upload_to='images/parcels/%Y/%m/%d/', default='', blank=True)
    photo_order = models.ImageField('Фотография заказа', upload_to='images/parcels/%Y/%m/%d/', default='', blank=True)

    date_publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    date_arrived = models.DateTimeField(blank=True, null=True)
    date_delivered = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('parcel_detail', kwargs={'parcel_id': self.pk})

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField('Магазин', max_length=50)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name