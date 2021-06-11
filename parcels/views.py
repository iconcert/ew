from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Parcel
from .forms import ParcelForm


def parcels_list(request):
    parcels = Parcel.objects.all().select_related('store')
    paginator = Paginator(parcels, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'parcels/index.html', {'parcels': page_obj})


def parcel_detail(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    return render(request, 'parcels/parcel.html', {'parcel': parcel})


def parcel_add(request):
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
    return render(request, 'parcels/parcel_add.html', {'form': form})


def parcel_edit(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    if request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES, instance=parcel)
        if form.is_valid():
            form.save()
            parcel = form.save(commit=False)
            parcel.save()
            return redirect(parcel)
    else:
        form = ParcelForm(instance=parcel)
    return render(request, 'parcels/parcel_edit.html', {'form': form})