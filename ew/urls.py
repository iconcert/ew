"""ew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from parcels.views import parcels_list, parcel_detail, parcel_add, parcel_edit
from news.views import news_list, news_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parcels_list, name='home'),
    path('parcel/<int:parcel_id>/', parcel_detail, name='parcel_detail'),
    path('parcel/<int:parcel_id>/edit/', parcel_edit, name='parcel_edit'),
    path('parcel/parcel-add/', parcel_add, name='parcel_add'),
    #подключить инклуд
    path('novosti/', news_list, name='news'),
    path('novosti/<int:new_id>/', news_detail, name='new')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
