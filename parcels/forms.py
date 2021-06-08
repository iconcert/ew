from django import forms
from .models import Parcel, Store


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        #exclude = ['user_warehouse']
        #fields = '__all__'
        fields = [
            'volume_weight',
            'enter_manually',
            'name',
            'tracking_number',
            'comment',
            'store',
            'status',
            'warehouse',
           # 'user_warehouse',
            'photo_parcel'
        ]
        widgets = {
            'volume_weight': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enter_manually': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'tracking_number': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'store': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'warehouse': forms.Select(attrs={'class': 'form-select'}),
            'photo_parcel': forms.FileInput(attrs={'class': 'form-control'}),
        }


'''
class ParcelForm(forms.Form):
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
    volume_weight = forms.BooleanField(label='Обьемный вес', initial=True, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    enter_manually = forms.BooleanField(label='Ввести вручную', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tracking_number = forms.CharField(label='Трекинг номер', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    store = forms.ModelChoiceField(label='Магазин', empty_label='--Выберите--', queryset=Store.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.ChoiceField(label='Статус', choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    warehouse = forms.ChoiceField(label='Склад', choices=WAREHOUSE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


    #user_warehouse = forms.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')
    #user_client = forms.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='+')
'''