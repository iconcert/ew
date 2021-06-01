from django.shortcuts import render, get_object_or_404
from .models import Parcel


def parcels_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcels/index.html', {'parcels': parcels})


def parcel_detail(request, parcel_id):
    parcel = get_object_or_404(Parcel, pk=parcel_id)
    return render(request, 'parcels/parcel.html', {'parcel': parcel})