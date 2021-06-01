from django import forms
from .models import Store


class ParcelForm(forms.Form):
    STATUS_CHOICES = (
        ('1', 'Проверяется'),
        ('2', 'Ждем на склад'),
        ('3', 'На складе'),
        ('4', 'Отправлена'),
        ('5', 'На обработке'),
        ('6', 'Прибыла в Бишкек'),
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
    volume_weight = forms.BooleanField()
    enter_manually = forms.BooleanField()

    name = forms.CharField(max_length=50)

    store = forms.ModelChoiceField(queryset=Store.objects.all())
    tracking_number = forms.CharField(max_length=50)

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    warehouse = forms.ChoiceField(choices=WAREHOUSE_CHOICES)

    comment = forms.CharField()

    #user_warehouse = forms.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')
    #user_client = forms.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')