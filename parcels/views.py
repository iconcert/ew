from django.shortcuts import render, get_object_or_404, redirect
from .models import Parcel
from .forms import ParcelForm


def parcels_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcels/index.html', {'parcels': parcels})


def parcel_detail(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    return render(request, 'parcels/parcel.html', {'parcel': parcel})


def add_parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            #parcel = Parcel.objects.create(**form.cleaned_data) #только для class ParcelForm(forms.Form)
            parcel = form.save(commit=False)  # Пока не записывать изменения в БД
            parcel.user_warehouse = request.user
            parcel.save()  # Теперь можно записать
            return redirect(parcel)
    else:
        form = ParcelForm()
    return render(request, 'parcels/add_parcel.html', {'form': form})